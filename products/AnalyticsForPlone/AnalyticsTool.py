## -*- coding: utf-8 -*-
## Copyright (C)2006 Ingeniweb

## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; see the file COPYING. If not, write to the
## Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import time
import re
import os


from Acquisition import aq_base
from AccessControl import ClassSecurityInfo
from Globals import InitializeClass
from OFS.SimpleItem import SimpleItem
from OFS.PropertyManager import PropertyManager
from Products.PageTemplates.PageTemplateFile import PageTemplateFile

from Products.CMFCore.utils import UniqueObject

try: # New CMF
    from Products.CMFCore import permissions as CMFCorePermissions
except: # Old CMF. Only necessary for Plone versions < 2.5
    from Products.CMFCore import CMFCorePermissions

from Products.CMFPlone.interfaces.BrowserDefault import IBrowserDefault

from Products.AnalyticsForPlone import config

# security.declareProtected(Permission, methodNameAsString)
# security.declarePrivate(methodNameAsString)
# security.declarePublic(methodNameAsString)
# default manager permission is CMFCorePermissions.ManagePortal

class AnalyticsTool(PropertyManager, UniqueObject, SimpleItem):
    """
        This tool holds the Google Analytics Id inserted on each page.
    """
    id = 'analytics_tool'
    meta_type = 'AnalyticsTool'
    plone_tool = 1
    title = "Google Analytics Tool"
    filter_analytics = False
    filter_on_view = True
    filter_on_templates = []
    google_url = "http://www.google-analytics.com/ga.js"
    google_ssl_url = "https://ssl.google-analytics.com/ga.js"

    _properties = (
        {'id':'uacct', 'type': 'string', 'mode':'w'},
        {'id':'filter_analytics', 'type': 'boolean', 'mode':'w'},
        {'id':'filter_on_view', 'type': 'boolean', 'mode':'w'},
        {'id':'filter_on_templates', 'type': 'lines', 'mode':'w'},
        {'id':'google_url', 'type': 'string', 'mode':'w'},
        {'id':'google_ssl_url', 'type': 'string', 'mode':'w'},
    )

    overviewPath = os.path.join(os.path.dirname(__file__), 'zmi', 'overview')

    manage_options = (

        ({'label' : 'Overview',
          'action' : 'overview'
          },)

        + PropertyManager.manage_options
        + SimpleItem.manage_options
    )

    security = ClassSecurityInfo()
    overview = PageTemplateFile(overviewPath)
    security.declareProtected(CMFCorePermissions.ManagePortal, 'overview')

    security.declarePrivate('manage_afterAdd')
    def manage_afterAdd(self, item, container) :
        SimpleItem.manage_afterAdd(self, item, container)

        self.uacct = ""
        self.filter_analytics = False
        self.filter_on_view = True
        self.filter_on_templates = []

    def doAnalytics(self, context, request):
        """Returns True if analytics will be done on this context

        @param context: Traversed object
        @param request: HTTPRequest
        """

        # Check if you do analytics or not
        if not self.filter_analytics:
            return True

        published_obj = request.get('PUBLISHED', None)

        if published_obj is None:
            return False

        # Get current template id
        template_id = aq_base(published_obj).getId()

        # Get view template_id
        if IBrowserDefault.isImplementedBy(context):
            # For content types implementing new FTI
            view_template_id = context.getLayout()
        else:
            # For old content types
            view_template_id = context.lookupTypeAction('view')

            if not view_template_id:
                view_template_id = context.lookupTypeAction('folderlisting')

        # Get portal_type of context
        portal_type = None

        if hasattr(aq_base(context), 'portal_type'):
            portal_type = context.portal_type

        # Check if we analyse this template or not
        result = False

        if self.filter_on_view and template_id == view_template_id:
            result = True
        elif self.filter_on_templates:
            template_filter = '%s|%s' % (portal_type, template_id)

            if template_id in self.filter_on_templates or\
               template_filter in self.filter_on_templates:
                return True

        return result

InitializeClass(AnalyticsTool)

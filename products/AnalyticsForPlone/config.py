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

# CMF imports
from Products.CMFCore import permissions

GLOBALS = globals()
PROJECTNAME = "AnalyticsForPlone"
SKIN_NAME = "analyticsforplone"

CONFIG_PERMISSION = permissions.ManagePortal

# Configlets to be added to control panels or removed from them
configlets = (
    {
        'id'         : 'AnalyticsConf',
        'name'       : 'Analytics for Plone',
        'action'     : 'string:${portal_url}/conf_analytics',
        'condition'  : '',
        'category'   : 'Products',    # section to which the configlet should be added:
                                      # (Plone,Products,Members)
        'visible'    : 1,
        'appId'      : PROJECTNAME,
        'permission' : 'ManagePortal',
        'imageUrl'   : 'analytics_icon.gif',
    },
)


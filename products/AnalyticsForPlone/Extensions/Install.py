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

from cStringIO import StringIO
from Products.CMFCore.DirectoryView import addDirectoryViews
from Products.CMFCore.utils import getToolByName
from Products.AnalyticsForPlone import config
from Products.AnalyticsForPlone.AnalyticsTool import AnalyticsTool

import string



def installSubSkin(context, skinFolder, outStream):
    """
        Install a subskin in portal_skins
    """
    skinsTool = getToolByName(context, 'portal_skins')
    for skin in skinsTool.getSkinSelections() :
        path = skinsTool.getSkinPath(skin)
        path = map(string.strip, string.split(path, ','))
        if not skinFolder in path:
            try:
                path.insert(path.index('custom') + 1, skinFolder)
            except ValueError:
                path.append(skinFolder)
            path = string.join(path, ', ')
            skinsTool.addSkinSelection(skin, path)
            outStream.write('Subskin successfully installed into %s.\n' % skin)
        else:
            outStream.write('*** Subskin was already installed into %s.\n' % skin)

def addTool(self) :
    # Check that the tool has not been added using its id
    if not hasattr(self, AnalyticsTool.id) :
        addTool = self.manage_addProduct[config.PROJECTNAME].manage_addTool
        # Add the tool by its meta_type
        addTool(AnalyticsTool.meta_type)

def installConfiglet(self, out) :
    configTool = getToolByName(self, 'portal_controlpanel', None)
    if configTool:
        for conf in config.configlets:
            configTool.registerConfiglet(**conf)
            out.write('Added configlet %s\n' % conf['id'])

def uninstallConfiglet(self, out) :
    configTool = getToolByName(self, 'portal_controlpanel', None)
    if configTool:
        for conf in config.configlets:
            configTool.unregisterConfiglet(conf['id'])
            out.write('Removed configlet %s\n' % conf['id'])

def registerJavaScript(self, out):
    jsTool = getToolByName(self, 'portal_javascripts', None)
    ## Why inline is True ?
    ## Google Analytics is foolproof and so it checks that the code it delivers
    ## is really inserted (like copy pasted) in all the pages.
    ## With Plone, it's a little bit more complicated since adding code
    ## snippet anywhere isn't not as easy as this. So a javascript insert the
    ## google analytics code on the fly (to avoid modifying the main template).
    ## The inline option is only here to force the google id (uacct) to be
    ## physically present on the page.
    if jsTool:
        jsTool.manage_addScript(
            "analytics.js",
            cookable=False,
            enabled=True,
            inline=True,
            expression='python:portal.analytics_tool.doAnalytics(object, request)',
        )
        out.write("Javascript registered succesfully.\n")


def install(self) :
    outStream = StringIO()
    skinsTool = getToolByName(self, 'portal_skins')
    addDirectoryViews(skinsTool, 'skins', config.GLOBALS)
    installSubSkin(self, config.SKIN_NAME, outStream)
    addTool(self)
    installConfiglet(self, outStream)
    registerJavaScript(self, outStream)
    return outStream.getvalue()

def uninstall(self) :
    outStream = StringIO()
    uninstallConfiglet(self, outStream)
    return outStream.getvalue()

"""
this is used by portal_quickinstaller to install the product
"""

__author__ = 'I-Ling Lin'
__docformat__ = 'restructuredtext'


# Python imports
from StringIO import StringIO

# CMF imports
from Products.CMFCore.utils import getToolByName

# Archetypes imports
from Products.Archetypes.public import listTypes
from Products.Archetypes.Extensions.utils import installTypes, install_subskin

# Product imports
from Products.LandingPage.config import PROJECTNAME, GLOBALS


def configureTypes(self, out):
    """Register new types and configure them.
    """

    # install types
    installTypes(self, out, listTypes(PROJECTNAME), PROJECTNAME)
    print >> out, "installed types."

    # enable portal_factory to create temporary content
    factory = getToolByName(self, "portal_factory")
    types = factory.getFactoryTypes().keys()
    for t in [ "LandingPage", "TextBlock" ]:
        if t not in types:
            print >> out, "Adding %s to factory types" % t
            types.append(t)
    factory.manage_setPortalFactoryTypes(listOfTypeIds = types)


def install(self):
    """install LandingPage product:
    install content types, skin layer, stylesheet
    set up global properties, enable the portal factory and set up form controller
    actions for the widget actions.
    uses StringIO() to return a success message. 
    """

    out = StringIO()
    print >> out, "Installing %s..." % PROJECTNAME

    # install types, enable portal_factory
    configureTypes(self, out)

    # install skin
    install_subskin(self, out, GLOBALS)
    print >> out, "installed skin."

    propsTool = getToolByName(self, 'portal_properties')
    siteProperties = getattr(propsTool, 'site_properties')

    # Add the TextBlock type to types_not_searched
    # (this is configurable via the Search settings control panel)
    typesNotSearched = list(siteProperties.getProperty('types_not_searched'))
    if 'TextBlock' not in typesNotSearched:
        typesNotSearched.append('TextBlock')
    siteProperties.manage_changeProperties(types_not_searched = typesNotSearched)
    print >> out, "Added TextBlock to types_not_searched"

    # Add LandingPage to kupu's linkable type
    kupuTool = getToolByName(self, 'kupu_library_tool')
    linkable = list(kupuTool.getPortalTypesForResourceType('linkable'))
    if 'LandingPage' not in linkable:
        linkable.append('LandingPage')
    # kupu_library_tool has an idiotic interface, basically written purely to
    # work with its configuration page. :-(
    kupuTool.updateResourceTypes(({'resource_type' : 'linkable',
                                   'old_type'      : 'linkable',
                                   'portal_types'  :  linkable},))
    print >> out, "Added LandingPage to kupu's linkable type"

    print >> out, "Successfully installed %s." % PROJECTNAME
    return out.getvalue()

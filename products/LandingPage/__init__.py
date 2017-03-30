"""
initialize LandingPage product
"""

__author__ = 'I-Ling Lin'
__docformat__ = 'restructuredtext'


# CMF imports
from Products.CMFCore import utils
from Products.CMFCore.DirectoryView import registerDirectory

# Archetypes imports
from Products.Archetypes.public import process_types, listTypes

# Plone/Zope imports
try:
    from Products.CMFPlone.interfaces import IPloneSiteRoot
    from Products.GenericSetup import EXTENSION, profile_registry
    HAS_GENERICSETUP = True
except ImportError:
    HAS_GENERICSETUP = False

# Product imports
import LandingPage, TextBlock
from Products.LandingPage.config import *
from Products.LandingPage.permissions import ADD_CONTENT_PERMISSION

# register the skins and global directories as File System Directory Views in CMF
# so we can view these files and directory structures via the ZMI as if they were in Zope
# i.e. they can be added to portal_skins
registerDirectory(SKINS_DIR, GLOBALS)

def initialize(context):
    """initialization method
    """

    # generate the content types, constructors, and FTIs
    content_types, constructors, ftis = process_types(listTypes(PROJECTNAME), PROJECTNAME)

    # instatiates an object of the type ContentInit (from the CMFCore) and register the types in the CMF
    # or permission = DEFAULT_ADD_CONTENT_PERMISSION,
    utils.ContentInit(PROJECTNAME + ' Content',
                      content_types      = content_types,
                      permission         = ADD_CONTENT_PERMISSION,
                      extra_constructors = constructors,
                      fti                = ftis,
                      ).initialize(context)

    if HAS_GENERICSETUP:
        profile_registry.registerProfile(PROJECTNAME,
                                         PROJECTNAME,
                                         'Extension profile for default setup',
                                         'profiles/default',
                                         PROJECTNAME,
                                         EXTENSION,
                                         for_=IPloneSiteRoot)

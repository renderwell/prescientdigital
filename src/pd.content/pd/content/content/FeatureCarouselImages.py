# -*- coding: utf-8 -*-

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
from pd.content.interfaces import IFeatureCarouselImages
from plone.portlets.interfaces import ILocalPortletAssignable

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin
from Products.ATContentTypes.atct import ATFolder, ATFolderSchema

from pd.content.config import *

schema = Schema((


),
)

FeatureCarouselImages_schema = ATFolderSchema.copy() + \
    schema.copy()

class FeatureCarouselImages(ATFolder):
    """
    """
    security = ClassSecurityInfo()

    implements(IFeatureCarouselImages, ILocalPortletAssignable)

    meta_type = 'FeatureCarouselImages'
    _at_rename_after_creation = True

    schema = FeatureCarouselImages_schema

    def exclude_from_nav(self):
        return True

registerType(FeatureCarouselImages, PROJECTNAME)

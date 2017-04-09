# -*- coding: utf-8 -*-

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
from pd.content.interfaces import ITestimonialFolder
from plone.portlets.interfaces import ILocalPortletAssignable

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin
from Products.ATContentTypes.atct import ATFolder, ATFolderSchema

from pd.content.config import *

schema = Schema((


),
)

TestimonialFolder_schema = ATFolderSchema.copy() + \
    schema.copy()

class TestimonialFolder(ATFolder):
    """
    """
    security = ClassSecurityInfo()

    implements(ITestimonialFolder, ILocalPortletAssignable)

    meta_type = 'TestimonialFolder'
    _at_rename_after_creation = True

    schema = TestimonialFolder_schema

    # Methods

registerType(TestimonialFolder, PROJECTNAME)

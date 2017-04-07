# -*- coding: utf-8 -*-

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
from pd.content.interfaces import ICaseStudyFolder
from plone.portlets.interfaces import ILocalPortletAssignable

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from pd.content.config import *

schema = Schema((


),
)

CaseStudyFolder_schema = OrderedBaseFolderSchema.copy() + \
    schema.copy()

class CaseStudyFolder(OrderedBaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(ICaseStudyFolder, ILocalPortletAssignable)

    meta_type = 'CaseStudyFolder'
    _at_rename_after_creation = True

    schema = CaseStudyFolder_schema

    # Methods

registerType(CaseStudyFolder, PROJECTNAME)

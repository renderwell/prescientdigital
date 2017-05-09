# -*- coding: utf-8 -*-

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
from pd.content.interfaces import IStyles
from plone.portlets.interfaces import ILocalPortletAssignable

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from pd.content.config import *

from Products.ATContentTypes.content import schemata

from plone.app.iterate.relation import WorkingCopyRelation


schema = Schema((
    TextField(
        name='styles',
        allowable_content_types=('text/plain', ),
        widget=TextAreaWidget(
            label='Styles',
            description='Styles',
            label_msgid='label_styles',
            description_msgid='description_styles',
            i18n_domain='pd.content',
            rows=100,
        ),
    ),
),
)

Styles_schema = BaseSchema.copy() + \
    schema.copy()


class Styles(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(IStyles, ILocalPortletAssignable)

    meta_type = 'Styles'
    _at_rename_after_creation = True

    schema = Styles_schema

    def exclude_from_nav(self):
        return True

registerType(Styles, PROJECTNAME)

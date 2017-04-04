# -*- coding: utf-8 -*-

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
from pd.content.interfaces import ITestimonial
from plone.portlets.interfaces import ILocalPortletAssignable

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from pd.content.config import *

from Products.ATContentTypes.content import schemata

from plone.app.iterate.relation import WorkingCopyRelation


schema = Schema((
    TextField(
        name='text',
        widget=TextAreaWidget(
            label="Text",
            label_msgid='label_testimonial_text',
            i18n_domain='pd.content',
        ),
    ),
    StringField(
        name='author',
        widget=StringField._properties['widget'](
            label="Author",
            label_msgid='label_testimonial_author',
            i18n_domain='pd.content',
        ),
    ),
    StringField(
        name='company',
        widget=StringField._properties['widget'](
            label="Company",
            label_msgid='label_testimonial_company',
            i18n_domain='pd.content',
        ),
    ),
),
)

Testimonial_schema = BaseSchema.copy() + \
    schema.copy()


class Testimonial(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(ITestimonial, ILocalPortletAssignable)

    meta_type = 'Testimonial'
    _at_rename_after_creation = True

    schema = Testimonial_schema

    # Methods


registerType(Testimonial, PROJECTNAME)

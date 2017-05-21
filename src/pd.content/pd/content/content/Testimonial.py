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
        name='quote',
        allowable_content_types=('text/plain', ),
        widget=TextAreaWidget(
            label='Quote',
            description='The testimonial text.',
            label_msgid='label_testimonial_quote',
            description_msgid='description_testimonial_quote',
            i18n_domain='pd.content',
        ),
    ),
    TextField(
        name='shortquote',
        allowable_content_types=('text/plain', ),
        widget=TextAreaWidget(
            label='Short Quote',
            description='An optional shorter version of the testimonial text. \
            If provided, it will be used in the testimonial slider, instead of \
            the (possibly) longer quote above. The longer quote will be listed \
            on the Testimonials page.',
            label_msgid='label_testimonial_quote',
            description_msgid='description_testimonial_quote',
            i18n_domain='pd.content',
        ),
    ),
    StringField(
        name='author',
        widget=StringField._properties['widget'](
            label='Author',
            label_msgid='label_testimonial_author',
            i18n_domain='pd.content',
        ),
    ),
    StringField(
        name='position',
        widget=StringField._properties['widget'](
            label='Position',
            description='The position of the author at their organisation',
            label_msgid='label_testimonial_position',
            description_msgid='description_testimonial_position',
            i18n_domain='pd.content',
        ),
    ),
    # StringField(
    #     name='organisation',
    #     widget=StringField._properties['widget'](
    #         label='Organisation',
    #         description='The organisation the author belongs to.',
    #         label_msgid='label_testimonial_organisation',
    #         description_msgid='description_testimonial_organisation',
    #         i18n_domain='pd.content',
    #     ),
    # ),
    BooleanField(
        name='featured',
        widget=BooleanField._properties['widget'](
            label='Featured',
            description='If selected, this testimonial will be shown in the slider on the homepage or elsewhere on the site where featured testimonials are displayed.',
            label_msgid='label_testimonial_featured',
            description_msgid='description_testimonial_featured',
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

# -*- coding: utf-8 -*-

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
from pd.content.interfaces import ICaseStudy
from plone.portlets.interfaces import ILocalPortletAssignable

from Products.ATContentTypes.content.document import ATDocument
from Products.ATContentTypes.content.document import ATDocumentSchema

from pd.content.config import *

from Products.ATContentTypes.content import schemata

from plone.app.iterate.relation import WorkingCopyRelation


schema = Schema((
    ImageField(
        name='image',
        searchable=False,
        sizes= {
            'large'   : (768, 768),
            'preview' : (400, 400),
            'mini'    : (200, 200),
            'thumb'   : (128, 128),
            'tile'    :  (64, 64),
            'icon'    :  (32, 32),
            'listing' :  (16, 16),
        },
        widget=ImageWidget(
            label='Image',
            label_msgid='label_casestudy_image',
            i18n_domain='pd.content',
        ),
    ),
    # TextField(
    #     name='body',
    #     allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
    #     widget=RichWidget(
    #         label='Body text',
    #         description='The main body text for the case study',
    #         allow_buttons=('bold', 'italic', 'bullist', 'link', 'unlink', 'code'),
    #         rows=20,
    #         label_msgid='label_casestudy_body',
    #         description_msgid='description_casestudy_body',
    #         i18n_domain='pd.content',
    #     ),
    #     default_output_type='text/html',
    #     searchable=1,
    # ),
    StringField(
        name='link',
        widget=StringField._properties['widget'](
            label='Link',
            description='Link to the relevant case study page',
            label_msgid='label_casestudy_link',
            description_msgid='description_casestudy_link',
            i18n_domain='pd.content',
        ),
    ),
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

CaseStudy_schema = ATDocumentSchema.copy() + \
    schema.copy()

CaseStudy_schema['description'].schemata = 'default'

class CaseStudy(ATDocument):
    """
    """
    security = ClassSecurityInfo()

    implements(ICaseStudy, ILocalPortletAssignable)

    meta_type = 'CaseStudy'
    _at_rename_after_creation = True

    schema = CaseStudy_schema

    # Methods


registerType(CaseStudy, PROJECTNAME)
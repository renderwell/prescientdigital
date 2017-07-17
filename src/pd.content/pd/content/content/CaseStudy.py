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
            description='Please upload an image of width 600px and height 400px',
            label_msgid='label_casestudy_image',
            description_msgid='description_casestudy_image',
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
    BooleanField(
        name='featured',
        widget=BooleanField._properties['widget'](
            label='Featured',
            description='If selected, this case study will be shown in the slider on the homepage or elsewhere on the site where featured case studies are displayed.',
            label_msgid='label_case_study_featured',
            description_msgid='description_case_study_featured',
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

    def exclude_from_nav(self):
        return True

registerType(CaseStudy, PROJECTNAME)

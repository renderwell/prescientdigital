# -*- coding: utf-8 -*-

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
from pd.content.interfaces import IBannerImage
from plone.portlets.interfaces import ILocalPortletAssignable

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

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
            label_msgid='label_bannerimage_image',
            description='Please provide an image with ratio 2:1, and at least 2000px wide',
            description_msgid='description_bannerimage_image',
            i18n_domain='pd.content',
        ),
    ),
),
)

BannerImage_schema = BaseSchema.copy() + \
    schema.copy()


class BannerImage(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(IBannerImage, ILocalPortletAssignable)

    meta_type = 'BannerImage'
    _at_rename_after_creation = True

    schema = BannerImage_schema

    # Methods


registerType(BannerImage, PROJECTNAME)

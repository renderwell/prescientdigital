from zope.component import adapts
from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content.document import ATDocument

from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import ISchemaExtender, IBrowserLayerAwareExtender

from pd.content.browser.interfaces import IPrescientDigitalTypesLayer


class ImageExtensionField(ExtensionField, atapi.ImageField):
    """ImageField for use with archetypes.schemaextender
    """

class TileImagePageExtender(object):
    adapts(ATDocument)
    implements(ISchemaExtender)

    fields = []
    layer = IPrescientDigitalTypesLayer

    fields.append(ImageExtensionField(
        'tileImage',
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
        widget=atapi.ImageWidget(
            label='Tile Image',
            description='Please upload an image of width 600px and height 400px',
            label_msgid='label_page_image',
            description_msgid='description_page_image',
            i18n_domain='pd.content',
        ),
    )
    )

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields

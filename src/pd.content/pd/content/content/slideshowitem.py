"""Definition of the SlideshowItem content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import schemata, link
from Products.Archetypes.atapi import StringField, ImageField
from Products.Archetypes.atapi import ImageWidget, StringWidget

from pd.content.interfaces import ISlideshowItem
from pd.content.config import PROJECTNAME

from Products.ATContentTypes.configuration import zconf
from pd.content import contentMessageFactory as _

from Products.validation.config import validation
from Products.validation.validators.SupplValidators import MaxSizeValidator
from Products.validation import V_REQUIRED

validation.register(MaxSizeValidator('checkImageMaxSize',
                                     maxsize=zconf.ATImage.max_file_size))

SlideshowItemSchema = link.ATLinkSchema.copy() + atapi.Schema((

    ImageField('image',
        required=True,
        storage=atapi.AnnotationStorage(),
        languageIndependent=True,
        max_size=zconf.ATNewsItem.max_image_dimension,
        sizes={'large': (768, 768),
               'preview': (400, 400),
              },
        validators=(('isNonEmptyFile', V_REQUIRED),
                    ('checkNewsImageMaxSize', V_REQUIRED)),
        widget=ImageWidget(
            description=_(u'help_slideshow_image',
                default=u'Set Image for Slideshow Item'),
            label=_(u'label_slideshow_image',
                default=u'Slideshow Image'),
            show_content_type=False)
        ),

    StringField(
        'detailtext',
        required=True,
        default=_(u'View Detail'),
        storage=atapi.AnnotationStorage(),
        widget=StringWidget(
            label=_(u'view_detail_button_label',
                default=u'View Details Label'),
            description=_(u'help_detail_button_descr',
                default=u'Set Text for Detail View Button'))
        ),
))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

SlideshowItemSchema['title'].storage = atapi.AnnotationStorage()
SlideshowItemSchema['description'].storage = atapi.AnnotationStorage()
SlideshowItemSchema['remoteUrl'].storage = atapi.AnnotationStorage()
SlideshowItemSchema.moveField('remoteUrl', after='image')

SlideshowItemSchema['description'].widget.label = _(u'view_slideshow_descr',
        default='Description')
SlideshowItemSchema['remoteUrl'].widget.description = _(u'help_slideshow_url',
        default=u'Set Detail Link')
SlideshowItemSchema['remoteUrl'].widget.label = _(u'view_slideshow_url',
        default=u'URL')

schemata.finalizeATCTSchema(SlideshowItemSchema, moveDiscussion=False)


class SlideshowItem(link.ATLink):
    """SlideshowItem for ngcollection portlet carousel template"""
    implements(ISlideshowItem)

    meta_type = "SlideshowItem"
    schema = SlideshowItemSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    image = atapi.ATFieldProperty('image')

    remoteUrl = atapi.ATFieldProperty('remoteUrl')
    detailtext = atapi.ATFieldProperty('detailtext')

atapi.registerType(SlideshowItem, PROJECTNAME)

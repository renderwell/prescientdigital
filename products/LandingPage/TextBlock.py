"""
according to Martin Aspeli, the author of RichDocument:
Use the standard Document types for the attached text blocks is problmatic
because they gain their own workflows and become searchable as standard.
Instead, provide simple custom version of ATDocument here
"""

__author__ = 'I-Ling Lin'
__docformat__ = 'restructuredtext'


# Archetypes imports
from Products.Archetypes.public import *

# Product imports
from Products.LandingPage.config import *

# Other imports
from Products.ATContentTypes.content.base import ATCTContent
from Products.ATContentTypes.content.schemata import ATContentTypeSchema

# create content type's schema with a textfield and update default fields
BlockSchema  = ATContentTypeSchema.copy() + Schema((
    TextField("textBlock",
              required                = True,
              searchable              = True,
              primary                 = True,
              allowable_content_types = ('text/html', 'text/plain'),
              default_content_type    = 'text/html',
              default_output_type     = 'text/html',
              widget                  = RichWidget(
                  i18n_domain       = I18N_DOMAIN,
                  label             = "Text Block",
                  label_msgid       = "text_block_label",
                  description_msgid = "text_block",
                  description       = "A text block on the landing page.",)),))

BlockSchema['allowDiscussion'].schemata = 'default'
del BlockSchema["description"]
BlockSchema["title"].widget = StringWidget(i18n_domain       = I18N_DOMAIN,
                                           label             = "Title",
                                           label_msgid       = "textblock_title_label",
                                           description_msgid = "textblock_title",
                                           description       = "The title of a text block.")
BlockSchema.moveField("textBlock", after = "title")

class TextBlock(ATCTContent):
    """A text block, which essentially is a ATDocument
    but it is not allow to be added globally
    """

    # standard content type setupt
    schema = BlockSchema
    portal_type = meta_type = "TextBlock"
    archetype_name = "Text block"
    content_icon = "document_icon.gif"

    # views setup -- these are available from the 'display' menu
    #default_view = "textblock_view"
    #immediate_view = "textblock_view"
    #suppl_views = ()

    # description
    typeDescription = "A text block attached to a page. Can contain rich text."
    typeDescMsgId = "TextBlock_description_edit"

    # make sure we get title-to-id generation when an object is created
    _at_rename_after_creation  = True
    global_allow = False

    #__implements__ = (ATCTContent.__implements__,)

    def getTitle(self):
        return self.Title()

# activate the content type
registerType(TextBlock, PROJECTNAME)

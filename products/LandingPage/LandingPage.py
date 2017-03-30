"""
main module of the product
"""

__author__ = 'I-Ling Lin'
#__docformat__ = 'plaintext'
__docformat__ = 'restructuredtext'


# Zope imports
from AccessControl import getSecurityManager, ClassSecurityInfo

# CMF imports
#from Products.CMFCore import CMFCorePermissions
from Products.CMFCore import permissions as CMFCorePermissions
from Products.CMFCore.permissions import View

# Archetypes imports
from Products.Archetypes.public import *
from Products.Archetypes.interfaces.orderedfolder import IOrderedFolder

# Product imports
from Products.LandingPage.config import *

# Other imports
from Products.ATContentTypes.atct import ATFolder, ATFolderSchema
from Products.ATContentTypes.configuration import zconf

# copy the ATFolderSchema schema (to avoid modifying the original) and append our own fileds
# create content type's schema with a textfield and 2 booleanfields
LandingSchema  = ATFolderSchema.copy() + Schema((

    TextField("text",
              searchable = True,
              required   = True,
              primary=True,
              storage = AnnotationStorage(migrate=True),
              validators = ('isTidyHtmlWithCleanup',),
              #validators = ('isTidyHtml',),
              default_content_type = zconf.ATDocument.default_content_type,
              default_output_type = 'text/x-html-safe',
              allowable_content_types = zconf.ATDocument.allowed_content_types,
              widget = RichWidget(description = "The Body of the landing page.",
                                  description_msgid = "landing_body",
                                  label = "Body Text",
                                  label_msgid = "landing_bodylabel",
                                  rows = 25,
                                  i18n_domain = I18N_DOMAIN,
                                  allow_file_upload = zconf.ATDocument.allow_document_upload)),
    BooleanField("listTitles",
                 searchable  = False,
                 widget      = BooleanWidget(
                     i18n_domain       = I18N_DOMAIN,
                     label             = "Show the list of textblock titles",
                     label_msgid       = "landing_titlelistlabel",
                     description_msgid = "landing_titlelist",
                     description       = "Show a list of all textblock titles at the top of the text blocks.",)),
    BooleanField("displayTextBlocks",
                 searchable = False,
                 default    = True,
                 widget     = BooleanWidget(
                     i18n_domain       = I18N_DOMAIN,
                     label             = "Show the text blocks",
                     label_msgid       = "landing_textblockslabel",
                     description_msgid = "landing_textblocks",
                     description       = "Show the individual text blocks in full.",)),
    ))


# activate the content type by registering it
class LandingPage(ATFolder):
    """A Page which may contain blocks of sub-content, as a folderish object
    first a folderish object, and second get all the fields from ATDocument
    """

    # security setup
    security = ClassSecurityInfo()
    security.declarePublic("listFolderContents")

    # standard content type setup
    schema = LandingSchema
    content_icon = "landing_icon.gif"
    portal_type = meta_type = PROJECTNAME
    filter_content_types = True
    allowed_content_types = ( "TextBlock", )
    archetype_name          = "Landing page"

    # views setup -- these are available from the 'display' menu
    default_view = "landing_tabular_view"
    immediate_view = "landing_tabular_view"
    suppl_views = ( "landingpage_view", "landing_summary_view", )

    # description
    typeDescription = "A page that may contain rich text and a set of rich text sub-contents."
    typeDescMsgId = "LandingPage_description_edit"

    # get the action tabs
    actions = ({'id' : "view",
                'name' : "View",
                'action' : "string:${object_url}/landingpage_view",
                'permissions' : (CMFCorePermissions.View,)},
               {'id' : "addblock",
                'name' : "Add Block",
                'action' : "string:${object_url}/createObject?type_name=TextBlock",
                'permissions' : (CMFCorePermissions.ModifyPortalContent,)},
               )

    def post_validate(self, REQUEST = None, errors = {}):
        """Custom validator to check if either listTitles or displayTextBlocks is set.
        """
        if not (int(REQUEST.form.get("listTitles", 1)) or int(REQUEST.form.get("displayTextBlocks", 1))):
            errors["listTitles"] = "Please select one of the show the text block titles or show the entire text blocks option"

    security.declareProtected(View, 'CookedBody')
    def CookedBody(self, stx_level='ignored'):
        """CMF compatibility method
        """
        return self.getText()


registerType(LandingPage, PROJECTNAME)

from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
from zope import schema
from zope.component import getUtility, getMultiAdapter
from zope.formlib import form
from zope.interface import implements
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFPlone import PloneMessageFactory as _

from plone.app.vocabularies.catalog import SearchableTextSourceBinder
from plone.app.form.widgets.wysiwygwidget import WYSIWYGWidget
from plone.app.form.widgets.uberselectionwidget import UberSelectionWidget
from Products.ATContentTypes.interface import IATImage

try:
    from plone.namedfile.interfaces import IImageScaleTraversable
    provides = [IATImage.__identifier__, IImageScaleTraversable.__identifier__]
except ImportError:
    IImageScaleTraversable = None
    provides = IATImage.__identifier__


class IParallaxPortlet(IPortletDataProvider):
    """Shows content on a background image with parallax effect.
    """
    js_hook_id = schema.TextLine(
        title=_(u"Javascript Hook ID"),
        description=_(u"Assign a unique element id that can be used as a hook for javascript"),
        required=False
    )

    text = schema.Text(
        title=_(u"Text"),
        description=_(u"The portlet body text."),
        required=False
    )

    background_image = schema.Choice(
        title=_(u"Background image"),
        description=_(u"Find the image"),
        required=False,
        source=SearchableTextSourceBinder({'object_provides' : provides})
    )

    center_text = schema.Bool(
        title=_(u"Center Text"),
        description=_(u"Tick this box if you simply want a short paragraph of text, centred in the parallax portlet."),
        required=False,
        default=False
    )


class Assignment(base.Assignment):
    implements(IParallaxPortlet)

    js_hook_id = None
    center_text = None

    def __init__(self, js_hook_id=u"", text=u"", background_image=None, center_text=u""):
        """Initialize all variables."""

        self.js_hook_id = js_hook_id
        self.text = text
        self.background_image = background_image
        self.center_text = center_text


class Renderer(base.Renderer):
    render = ViewPageTemplateFile('parallaxportlet.pt')

    def __init__(self, *args):
        base.Renderer.__init__(self, *args)
        portal_state = getMultiAdapter((self.context, self.request), name=u'plone_portal_state')
        self.portal_url = portal_state.portal_url()
        self.portal = portal_state.portal()

    def portlet_style(self):
        """Generate background image style.

        Note: ``background_image`` uses the uberselection-widget
        and does not return an object (unlike Archetypes reference
        fields).
        """

        image_path = self.data.background_image

        if image_path is None or len(image_path)==0:
            return None
        # The portal root is never a image

        if image_path[0]=='/':
            image_path = image_path[1:]
        image = self.portal.restrictedTraverse(image_path, default=None)

        if IImageScaleTraversable and IImageScaleTraversable.providedBy(image):
            try:
                view = image.restrictedTraverse('@@images')
                view = view.__of__(image)
                return view.tag('image')
            except:
                return None
        elif IATImage.providedBy(image) and image.getImage() is not None:
            # return image.tag()
            return 'background: url(%s/image) no-repeat fixed' % image.absolute_url()
        else:
            return None


class AddForm(base.AddForm):
    form_fields = form.Fields(IParallaxPortlet)
    form_fields['text'].custom_widget = WYSIWYGWidget
    form_fields['background_image'].custom_widget = UberSelectionWidget

    label = _(u"Add Parallax Portlet")
    description = _(u"Shows content on a background image with parallax effect.")

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    form_fields = form.Fields(IParallaxPortlet)
    form_fields['text'].custom_widget = WYSIWYGWidget
    form_fields['background_image'].custom_widget = UberSelectionWidget

    label = _(u"Edit Parallax Portlet")
    description = _(u"Shows content on a background image with parallax effect.")

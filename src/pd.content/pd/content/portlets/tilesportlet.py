from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
from zope import schema
from zope.component import getUtility, getMultiAdapter
from zope.formlib import form
from zope.interface import implements
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFPlone import PloneMessageFactory as _

from plone.app.vocabularies.catalog import SearchableTextSourceBinder
import plone.api


class ITilesPortlet(IPortletDataProvider):
    """Display links to pages as a grid of tiles
    """
    tilesTitle = schema.TextLine(
        title=_(u"Title"),
        description=_(u"Please provide an optional title for the tile grid section."),
        required=False
    )

    pages = schema.Text(
        title=_(u"Pages"),
        description=_(u"Please enter the urls of pages you wish to display as a grid of tiles. Please enter them one per line, and provide the full path in the form '/articles/the-master-ingredients-for-a-great-intranet', starting with the first '/' as the root of the site"),
        required=True
    )


class Assignment(base.Assignment):
    implements(ITilesPortlet)

    def __init__(self, tilesTitle=u"", pages=u""):
        """Initialize all variables."""
        self.tilesTitle = tilesTitle
        self.pages = pages


class Renderer(base.Renderer):
    render = ViewPageTemplateFile('tilesportlet.pt')

    def get_title(self):
        return self.data.tilesTitle

    def get_tiles(self):
        tiles = []
        paths = self.data.pages.split('\n')
        portal_url = plone.api.portal.get().absolute_url()

        for path in paths:
            if path:
                try:
                    page = plone.api.content.get(path)
                    if page:
                        title = page.Title()
                        url = page.absolute_url()
                        img_url = '%s/tileImage' % url

                        image = getattr(page, 'tileImage', None)
                        if not image:
                            img_url = '%s/++resource++pd.content.images/default-tile-image.png' % portal_url

                        tile = {
                            'title': title,
                            'url': url,
                            'img_url': img_url
                            }
                        tiles.append(tile)
                    else:
                        return
                except:
                    return

        return tiles


class AddForm(base.AddForm):
    form_fields = form.Fields(ITilesPortlet)

    label = _(u"Add Tiles Portlet")
    description = _(u"Display links to pages as a grid of tiles")

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    form_fields = form.Fields(ITilesPortlet)

    label = _(u"Edit Tiles Portlet")
    description = _(u"Display links to pages as a grid of tiles")

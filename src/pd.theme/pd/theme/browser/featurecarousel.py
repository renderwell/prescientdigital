from zope.component import getMultiAdapter
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from Products.CMFCore.utils import getToolByName
from plone.app.layout.navigation.defaultpage import isDefaultPage


class FeatureCarousel(ViewletBase):
    render = ViewPageTemplateFile('featurecarousel.pt')

    def default_page(self):
        return isDefaultPage(self.context.aq_parent, self.context)

    def items(self):
        context = self.context

        portal = self.context.portal_url.getPortalObject()
        catalog = getToolByName(self.context, 'portal_catalog')

        portal_properties = getToolByName(self.context, 'portal_properties')
        navtree_properties = getattr(portal_properties, 'navtree_properties')
        blacklist = navtree_properties.getProperty('metaTypesNotToList', ())

        folderish = context.isPrincipiaFolderish
        folder = folderish and context or context.aq_parent
        item_brains = folder.getFolderContents()

        nav_items = [i for i in item_brains if i.portal_type not in blacklist and not i.exclude_from_nav]

        image_folder_brain = portal.getFolderContents({'portal_type':'FeatureCarouselImages'})
        image_folder = len(image_folder_brain) > 0 and image_folder_brain[0].getObject() or None

        image_urls = []
        default_image_url = ''
        if image_folder:
            image_urls = [i.getURL() for i in image_folder.getFolderContents({'portal_type': 'Image'})]

        has_images = len(image_urls) > 0

        items = []
        count = 0
        for i in nav_items:
            info = {}

            info['title'] = i.Title

            description = i.Description
            words = description.split(' ')
            if len(words) > 15:
                description = '%s ...' % ' '.join(words[:15])
            info['description'] = '%s [read more]' %    description

            info['url'] = i.getURL()

            if has_images:
                if count > len(image_urls) - 1:
                    count = 0
                info['image'] = '%s/image' % image_urls[count]
                count += 1

            items.append(info)

        return items

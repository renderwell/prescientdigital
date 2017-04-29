from zope.component import getMultiAdapter
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from plone.memoize import view
from Products.CMFCore.utils import getToolByName
from plone.memoize.instance import memoize
from plone.app.layout.navigation.defaultpage import isDefaultPage


class BannerImage(ViewletBase):
    render = ViewPageTemplateFile('bannerimage.pt')

    def default_page(self):
        return isDefaultPage(self.context.aq_parent, self.context)

    def banner_style(self):
        context = self.context
        folder = self.default_page() and context.aq_parent or context
        brains = folder.getFolderContents({'portal_type': 'BannerImage'})
        banner_image = len(brains) > 0 and brains[0] or None

        banner_style = ""
        if banner_image:
            banner_style = 'background-image: url(%s/image)' % banner_image.getURL()

        return banner_style

    def show(self):
        path_length = len(self.context.getPhysicalPath())

        if self.default_page() and path_length == 4:
            return True
        elif path_length == 3:
            return True

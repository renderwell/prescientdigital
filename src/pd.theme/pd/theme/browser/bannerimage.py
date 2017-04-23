from zope.component import getMultiAdapter
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from plone.memoize import view
from Products.CMFCore.utils import getToolByName
from plone.memoize.instance import memoize
from plone.app.layout.navigation.defaultpage import isDefaultPage


class BannerImage(ViewletBase):
    render = ViewPageTemplateFile('bannerimage.pt')

    def banner_image_url(self):
        return '%s/banner-image/image' % context.absolute_url()

    def show(self):
        default_page = isDefaultPage(self.context.aq_parent, self.context)
        path_length = len(self.context.getPhysicalPath())

        if default_page and path_length == 4:
            return True
        elif path_length == 3:
            return True

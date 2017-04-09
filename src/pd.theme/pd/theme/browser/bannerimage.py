from zope.component import getMultiAdapter
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from plone.memoize import view
from Products.CMFCore.utils import getToolByName
from plone.memoize.instance import memoize


class BannerImage(ViewletBase):
    render = ViewPageTemplateFile('bannerimage.pt')

    def get_banner_image(self):
        return 'banner image'

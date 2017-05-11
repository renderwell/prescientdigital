from zope.component import getMultiAdapter
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from plone.memoize import view
from Products.CMFCore.utils import getToolByName
from plone.memoize.instance import memoize
from plone.app.layout.navigation.defaultpage import isDefaultPage
import plone.api


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
            # banner_style = 'background-image: url(%s/image)' % banner_image.getURL()

            banner_image_object = banner_image.getObject()

            scale_util = plone.api.content.get_view('images', banner_image_object, self.request)

            image = scale_util.scale('image', width=640, height=320, direction='down')
            image_40 = scale_util.scale('image', width=1024, height=512, direction='down')
            image_64 = scale_util.scale('image', width=1200, height=600, direction='down')
            image_75 = scale_util.scale('image', width=1440, height=720, direction='down')
            image_90 = scale_util.scale('image', width=1900, height=950, direction='down')

            banner_style = "<style> \
              #top-banner \
              {{ \
                background-image: url({image_url}); \
              }} \
              @media print, screen and (min-width: 40em) {{ \
                #top-banner {{ \
                  background-image: url({image_40_url}); \
                }} \
                #top-banner .card {{ \
                  background-image: none; \
                }} \
              }} \
              @media print, screen and (min-width: 64em) {{ \
                #top-banner {{ \
                  background-image: url({image_64_url}); \
                }} \
              }} \
              @media screen and (min-width: 75em) {{ \
                #top-banner {{ \
                  background-image: url({image_75_url}); \
                }} \
              }} \
              @media screen and (min-width: 90em) {{ \
                #top-banner {{ \
                  background-image: url({image_90_url}); \
                }} \
              }} \
            </style>".format(image_url=image.url, \
                image_40_url=image_40.url, image_64_url=image_64.url, \
                image_75_url=image_75.url, image_90_url=image_90.url)

        return banner_style

    def show(self):
        path_length = len(self.context.getPhysicalPath())

        if self.default_page() and path_length == 4:
            return True
        elif path_length == 3:
            return True

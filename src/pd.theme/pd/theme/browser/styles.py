from zope.component import getMultiAdapter
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from Products.CMFCore.utils import getToolByName
from plone.app.layout.navigation.defaultpage import isDefaultPage


class StylesViewlet(ViewletBase):
    render = ViewPageTemplateFile('styles.pt')

    def get_styles(self):
        portal_catalog = getToolByName(self.context, 'portal_catalog')
        styles = portal_catalog(portal_type="Styles")
        if len(styles) > 0:
            styles_obj = styles[0].getObject()
            return styles_obj.getStyles()

    def show(self):
        portal_url = self.context.portal_url()
        return "localhost" not in portal_url and "admin" not in portal_url

from zope.component import getMultiAdapter
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from Products.CMFCore.utils import getToolByName
from plone.app.layout.navigation.defaultpage import isDefaultPage


class MarkerViewlet(ViewletBase):
    render = ViewPageTemplateFile('markerviewlet.pt')

    def default_page(self):
        return isDefaultPage(self.context.aq_parent, self.context)

    def top_section(self):
        default_page = self.default_page()
        path_length = len(self.context.getPhysicalPath())

        if default_page and path_length == 4:
            return True
        elif path_length == 3:
            return True

    def full_width(self):
        context = self.context
        folder = self.default_page() and context.aq_parent or context
        import pdb; pdb.set_trace()
        x=1
        return

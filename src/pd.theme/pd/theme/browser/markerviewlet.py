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
        path_length = len(self.context.getPhysicalPath())

        if self.default_page() and path_length == 4:
            return True
        elif path_length == 3:
            return True

    def second_level(self):
        path_length = len(self.context.getPhysicalPath())

        if self.default_page() and path_length == 5:
            return True
        elif path_length == 4:
            return True

    def is_folder(self):
        if self.default_page() or self.context.isPrincipiaFolderish:
            return True

    def drop_sidenav(self):
        if self.top_section() or (self.second_level() and not self.is_folder()):
            return True

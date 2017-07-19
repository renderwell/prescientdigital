from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from Products.CMFCore.utils import getToolByName
from datetime import datetime

class CopyRight(ViewletBase):
    render = ViewPageTemplateFile('copyright.pt')

    def get_year(self):
        return datetime.now().year

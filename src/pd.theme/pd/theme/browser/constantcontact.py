from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from Products.CMFCore.utils import getToolByName
from datetime import datetime

class ConstantContact(ViewletBase):
    render = ViewPageTemplateFile('constantcontact.pt')


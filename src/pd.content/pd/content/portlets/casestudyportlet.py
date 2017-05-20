from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
from zope import schema
from zope.component import getUtility, getMultiAdapter
from zope.formlib import form
from zope.interface import implements
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFPlone import PloneMessageFactory as _


class ICaseStudyPortlet(IPortletDataProvider):
    """A portlet which shows 3 featured case studies.
    """


class Assignment(base.Assignment):
    implements(ICaseStudyPortlet)

    title = _(u'label_casestudyportlet', default=u'Case Study Portlet')


class Renderer(base.Renderer):
    render = ViewPageTemplateFile('casestudyportlet.pt')

    def get_casestudies(self):
        """Get the case studies
        """
        casestudies = []

        for item in self.context.portal_catalog(portal_type='CaseStudy', featured=True, review_state="published", sort_on='getObjPositionInParent', sort_limit=3):
            obj = item.getObject()
            casestudy = {}
            casestudy['title'] = obj.Title()

            description = obj.Description()
            words = description.split(' ')
            if len(words) > 15:
                description = '%s ...' % ' '.join(words[:15])
            casestudy['description'] = description

            casestudy['image_url'] = '%s/image' % obj.absolute_url()
            casestudy['link'] = obj.getLink()
            casestudies.append(casestudy)

        return casestudies


class AddForm(base.AddForm):
    form_fields = form.Fields(ICaseStudyPortlet)
    label = _(u"Add CaseStudy Portlet")
    description = _(u"This portlet displays 3 featured case studies")

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    form_fields = form.Fields(ICaseStudyPortlet)
    label = _(u"Edit Case Study Portlet")
    description = _(u"This portlet displays 3 featured case studies")

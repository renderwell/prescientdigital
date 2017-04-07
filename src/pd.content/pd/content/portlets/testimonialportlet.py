from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
from zope import schema
from zope.component import getUtility, getMultiAdapter
from zope.formlib import form
from zope.interface import implements
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFPlone import PloneMessageFactory as _


class ITestimonialPortlet(IPortletDataProvider):
    """A portlet which shows up to 5 Testimonials in a slider.
    """


class Assignment(base.Assignment):
    implements(ITestimonialPortlet)

    title = _(u'label_testimonialportlet', default=u'Testimonial Portlet')


class Renderer(base.Renderer):
    render = ViewPageTemplateFile('testimonialportlet.pt')

    def get_testimonials(self):
        """Get the testimonials
        """
        testimonials = []
        colors = ['#2178b0', '#649c22', '#195a85']

        for idx, item in enumerate(self.context.portal_catalog(portal_type='Testimonial', featured=True, review_state="published", sort_on='getObjPositionInParent', sort_limit=5)):
            obj = item.getObject()
            testimonial = {}
            testimonial['quote'] = obj.getQuote()
            testimonial['author'] = obj.getAuthor()
            testimonial['position'] = obj.getPosition()
            testimonial['organization'] = obj.getOrganisation()
            testimonial['bgcolor'] = colors[idx % 3]
            testimonials.append(testimonial)

        return testimonials


class AddForm(base.AddForm):
    form_fields = form.Fields(ITestimonialPortlet)
    label = _(u"Add Testimonial Portlet")
    description = _(u"This portlet displays featured testimonials in a slider")

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    form_fields = form.Fields(ITestimonialPortlet)
    label = _(u"Edit Testimonial Portlet")
    description = _(u"This portlet displays featured testimonials in a slider")

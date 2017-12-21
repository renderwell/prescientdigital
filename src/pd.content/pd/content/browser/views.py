# coding: utf-8
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName

class CaseStudyView(BrowserView):
    pass

class CaseStudyFolderView(BrowserView):
    def get_casestudies(self):
        casestudies = []

        path = '/'.join(self.context.getPhysicalPath())

        for item in self.context.portal_catalog(portal_type='CaseStudy',
            path={'query':'/'.join(self.context.getPhysicalPath()), 'level':0},
            review_state="published",
            sort_on='getObjPositionInParent'):

            obj = item.getObject()
            casestudy = {}
            casestudy['title'] = obj.Title()

            description = obj.Description()
            words = description.split(' ')
            if len(words) > 15:
                description = '%s ...' % ' '.join(words[:15])
            casestudy['description'] = description

            casestudy['image_url'] = '%s/image' % obj.absolute_url()
            casestudy['link'] = obj.absolute_url()
            casestudies.append(casestudy)

        return casestudies

class TestimonialFolderView(BrowserView):
    def get_testimonials(self):
        testimonials = []

        path = '/'.join(self.context.getPhysicalPath())

        for item in self.context.portal_catalog(portal_type='Testimonial',
            path={'query':'/'.join(self.context.getPhysicalPath()), 'level':0},
            review_state="published",
            sort_on='getObjPositionInParent'):

            obj = item.getObject()
            testimonial= {}
            testimonial['title'] = obj.Title()
            testimonial['quote'] = obj.getQuote()
            testimonial['author'] = obj.getAuthor()
            testimonial['position'] = obj.getPosition()

            testimonials.append(testimonial)

        return testimonials

class TileGrid(BrowserView):
    def get_tiles(self):
        return 'njurrr'


class getCMFUIDs(BrowserView):
    def get_cmf_uids(self):
        catalog = getToolByName(self.context, 'portal_catalog')

        items = []

        for i in catalog():
            item_dict = {}

            cmf_uid = i.cmf_uid

            if cmf_uid:
                url = i.getURL()

                item_dict['cmf_uid'] = cmf_uid
                item_dict['url'] = url

                items.append(item_dict)

        items = sorted(items, key=lambda k: (k['cmf_uid']))

        items_list = []

        for i in items:
            cmf_uid = i['cmf_uid']
            url = i['url']
            items_list.append('%(cmf_uid)s: <a href=%(url)s target="_blank">%(url)s</a>' % {'cmf_uid': cmf_uid, 'url': url})

        return '<br />'.join(items_list)




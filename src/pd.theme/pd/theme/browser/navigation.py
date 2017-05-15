from plone.app.portlets.portlets import navigation
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from plone.app.layout.navigation.navtree import buildFolderTree, NavtreeStrategyBase
from zope.component import getMultiAdapter

class PDUtils:

    def isHome(self):
        portal_state = getMultiAdapter((self.context, self.request),
                                       name=u'plone_portal_state')
        purl = '%s/' % portal_state.portal().absolute_url()
        curl = self.request.get('ACTUAL_URL', '')
        return purl == curl

class PDMenu(PDUtils):

    def getMenu(self):
        portal_state = getMultiAdapter((self.context, self.request),
                                       name=u'plone_portal_state')
        portal_properties = getToolByName(self.context, 'portal_properties')
        navtree_properties = getattr(portal_properties, 'navtree_properties')

        query = {}
        query['path'] = {'query' : '/'.join(portal_state.portal().getPhysicalPath()), 'depth': 2 }

        blacklist = navtree_properties.getProperty('metaTypesNotToList', ())
        all_types = self.context.portal_catalog.uniqueValuesFor('portal_type')
        query['portal_type'] = [t for t in all_types if t not in blacklist]

        tree = buildFolderTree(self.context, obj=self.context, query=query, strategy=PDMenuNavigationStrategy())

        if tree and tree.has_key('children'):
            return tree['children']

        return []


class PDMenuNavigationStrategy(NavtreeStrategyBase):

    def nodeFilter(self, node):
        return (not node['item'].exclude_from_nav)

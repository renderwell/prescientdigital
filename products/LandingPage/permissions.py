"""
security permissions used in LandingPage product
"""

__author__ = 'I-Ling Lin'
__docformat__ = 'restructuredtext'

# CMF imports
#from Products.CMFCore import CMFCorePermissions
from Products.CMFCore import permissions as CMFCorePermissions

# Add permission
#ADD_CONTENT_PERMISSION = "PDMLandingPage: Add LandingPage"
DEFAULT_ADD_CONTENT_PERMISSION = "PDMLandingPage: Add PDMLandingPage - default"
#CMFCorePermissions.setDefaultRoles(ADD_CONTENT_PERMISSION, ('Manager', 'Owner',))
ADD_CONTENT_PERMISSION = CMFCorePermissions.AddPortalContent

# Edit/Delete a PDM Landing Page
EDIT_CONTENT_PERMISSION = "PDMLandingPage: Edit/Delete LandingPage"
#CMFCorePermissions.setDefaultRoles(EDIT_CONTENT_PERMISSION, ('Manager', 'Owner',))

# View a PDM Landing Page
VIEW_CONTENT_PERMISSION = "PDMLandingPage: View LandingPage"
#CMFCorePermissions.setDefaultRoles(VIEW_CONTENT_PERMISSION, ('Manager', 'Owner', 'Member', 'Anonymous'))

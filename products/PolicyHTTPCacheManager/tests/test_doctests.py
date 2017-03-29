"""
$Id: test_doctests.py 14058 2005-11-18 01:03:05Z dreamcatcher $
"""

import os
import sys

if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

# Load fixture
from Testing import ZopeTestCase
from Testing.ZopeTestCase import FunctionalDocFileSuite
from Products.CMFTestCase import CMFTestCase

CMFTestCase.installProduct('PageTemplates')
CMFTestCase.installProduct('StandardCacheManagers')
CMFTestCase.installProduct('PolicyHTTPCacheManager')
CMFTestCase.setupCMFSite()

class FunctionalTest(CMFTestCase.FunctionalTestCase): pass

def test_suite():
    import unittest
    suite = unittest.TestSuite()
    for fname in (
        'cache_manager.txt',
        ):
        suite.addTest(
            FunctionalDocFileSuite(
            fname,
            package='Products.PolicyHTTPCacheManager.tests',
            test_class=FunctionalTest))
    return suite

if __name__ == '__main__':
    framework(descriptions=0, verbosity=1)

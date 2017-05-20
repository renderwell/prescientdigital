# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger('PrescientDigitalContentTypes: setuphandlers')
from Products.CMFCore.utils import getToolByName
PROFILE_ID = 'profile-pd.content:default'

def isNotPrescientDigitalContentTypesProfile(context):
    return context.readDataFile("PrescientDigitalContentTypes_marker.txt") is None

def postInstall(context):
    """Called as at the end of the setup process. """
    if isNotPrescientDigitalContentTypesProfile(context): return
    portal = context.getSite()

    # Add catalog indexes
    setup = getToolByName(portal, 'portal_setup')
    setup.runImportStepFromProfile(PROFILE_ID, 'catalog')

    catalog = getToolByName(portal, 'portal_catalog')
    indexes = catalog.indexes()
    wanted = (
             ('featured', 'BooleanIndex'),
             )
    indexables = []
    for name, meta_type in wanted:
        if name not in indexes:
            catalog.addIndex(name, meta_type)
            indexables.append(name)
            logger.info("Added %s for field %s.", meta_type, name)
    if len(indexables) > 0:
        logger.info("Indexing new indexes %s.", ', '.join(indexables))
        catalog.manage_reindexIndex(ids=indexables)

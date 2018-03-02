# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from pkan.examplecontentfilter.content.pkan_item import IPkanItem
from pkan.examplecontentfilter.testing import PKAN_EXAMPLECONTENTFILTER_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class PkanItemIntegrationTest(unittest.TestCase):

    layer = PKAN_EXAMPLECONTENTFILTER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='pkan_item')
        schema = fti.lookupSchema()
        self.assertEqual(IPkanItem, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='pkan_item')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='pkan_item')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IPkanItem.providedBy(obj))

    def test_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='pkan_item',
            id='pkan_item',
        )
        self.assertTrue(IPkanItem.providedBy(obj))

# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from pkan.examplecontentfilter.testing import PKAN_EXAMPLECONTENTFILTER_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that pkan.examplecontentfilter is properly installed."""

    layer = PKAN_EXAMPLECONTENTFILTER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if pkan.examplecontentfilter is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'pkan.examplecontentfilter'))

    def test_browserlayer(self):
        """Test that IPkanExamplecontentfilterLayer is registered."""
        from pkan.examplecontentfilter.interfaces import (
            IPkanExamplecontentfilterLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IPkanExamplecontentfilterLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PKAN_EXAMPLECONTENTFILTER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get(userid=TEST_USER_ID).getRoles()
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['pkan.examplecontentfilter'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if pkan.examplecontentfilter is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'pkan.examplecontentfilter'))

    def test_browserlayer_removed(self):
        """Test that IPkanExamplecontentfilterLayer is removed."""
        from pkan.examplecontentfilter.interfaces import \
            IPkanExamplecontentfilterLayer
        from plone.browserlayer import utils
        self.assertNotIn(
           IPkanExamplecontentfilterLayer,
           utils.registered_layers())

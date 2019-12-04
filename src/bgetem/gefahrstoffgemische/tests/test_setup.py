# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from bgetem.gefahrstoffgemische.testing import BGETEM_GEFAHRSTOFFGEMISCHE_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that bgetem.gefahrstoffgemische is properly installed."""

    layer = BGETEM_GEFAHRSTOFFGEMISCHE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if bgetem.gefahrstoffgemische is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'bgetem.gefahrstoffgemische'))

    def test_browserlayer(self):
        """Test that IBgetemGefahrstoffgemischeLayer is registered."""
        from bgetem.gefahrstoffgemische.interfaces import (
            IBgetemGefahrstoffgemischeLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IBgetemGefahrstoffgemischeLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = BGETEM_GEFAHRSTOFFGEMISCHE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['bgetem.gefahrstoffgemische'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if bgetem.gefahrstoffgemische is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'bgetem.gefahrstoffgemische'))

    def test_browserlayer_removed(self):
        """Test that IBgetemGefahrstoffgemischeLayer is removed."""
        from bgetem.gefahrstoffgemische.interfaces import \
            IBgetemGefahrstoffgemischeLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IBgetemGefahrstoffgemischeLayer,
            utils.registered_layers())

# -*- coding: utf-8 -*-
from collective.js.galleria.testing import INTEGRATION_TESTING
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.registry.interfaces import IRegistry
from Products.CMFPlone.browser.admin import AddPloneSite
from Products.CMFPlone.controlpanel.browser.quickinstaller import ManageProductsView
from Products.CMFPlone.interfaces import IBundleRegistry
from Products.CMFPlone.utils import get_installer
from zope.component import getUtility

import unittest


PROJECTNAME = "collective.js.galleria"
JS = "++plone++collective.js.galleria/galleria.min.js"


class InstallTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.request = self.layer["request"]
        self.registry = getUtility(IRegistry)
        self.instaler = get_installer(self.portal, self.request)

    def test_installed(self):
        self.assertTrue(
            self.instaler.isProductInstalled(PROJECTNAME),
            "package appears not to have been installed",
        )

    def test_jsregistry(self):
        bundles = self.registry.collectionOfInterface(
            IBundleRegistry, prefix="plone.bundles"
        )
        bundle = bundles["galleria.js"]

        self.assertEqual(bundle.jscompilation, JS)

    def test_hide_upgrades_profiles(self):
        mp = ManageProductsView(self.portal, self.request)
        profiles = mp.get_available()
        package_profiles_availables = [
            profile["id"]
            for profile in profiles
            if profile["id"].startswith("collective.js.galleria")
        ]
        self.assertEqual([], package_profiles_availables)

    def test_hide_extensions_profiles(self):
        app = self.layer["app"]
        request = self.layer["request"]
        add_plone_site = AddPloneSite(app, request)
        profiles = add_plone_site.profiles()
        extensions_profiles = profiles["extensions"]
        profiles_ids = [profile["id"] for profile in extensions_profiles]
        package_profiles = [
            profile_id
            for profile_id in profiles_ids
            if profile_id.startswith(PROJECTNAME)
        ]
        self.assertEqual(["collective.js.galleria:default"], package_profiles)


class UninstallTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.request = self.layer["request"]
        self.registry = getUtility(IRegistry)
        self.instaler = get_installer(self.portal, self.request)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.instaler.uninstallProducts(products=[PROJECTNAME])

    def test_uninstalled(self):
        self.assertFalse(self.instaler.isProductInstalled(PROJECTNAME))

    def test_jsregistry_removed(self):
        bundles = self.registry.collectionOfInterface(
            IBundleRegistry, prefix="plone.bundles"
        )

        self.assertNotIn("galleria.js", bundles.keys())

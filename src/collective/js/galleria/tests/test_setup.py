# -*- coding: utf-8 -*-
from collective.js.galleria.testing import INTEGRATION_TESTING
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.registry.interfaces import IRegistry
from Products.CMFPlone.interfaces import IBundleRegistry
from Products.CMFPlone.utils import get_installer
from zope.component import getUtility

import unittest


PROJECTNAME = "collective.js.galleria"
JS = "++resource++collective.galleria.min.js"


class InstallTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.request = self.layer["request"]
        self.registry = getUtility(IRegistry)
        self.qi_tool = get_installer(self.portal, self.request)

    def test_installed(self):
        self.assertTrue(
            self.qi_tool.isProductInstalled(PROJECTNAME),
            "package appears not to have been installed",
        )

    def test_jsregistry(self):
        bundles = self.registry.collectionOfInterface(
            IBundleRegistry, prefix="plone.bundles"
        )
        bundle = bundles["galleria.js"]

        self.assertEqual(bundle.jscompilation, JS)


class UninstallTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.request = self.layer["request"]
        self.registry = getUtility(IRegistry)
        self.qi_tool = get_installer(self.portal, self.request)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.qi_tool.uninstallProducts(products=[PROJECTNAME])

    def test_uninstalled(self):
        self.assertFalse(self.qi_tool.isProductInstalled(PROJECTNAME))

    def test_jsregistry_removed(self):
        bundles = self.registry.collectionOfInterface(
            IBundleRegistry, prefix="plone.bundles"
        )

        self.assertNotIn("galleria.js", bundles.keys())

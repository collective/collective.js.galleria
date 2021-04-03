# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import IBundleRegistry
from Products.CMFPlone.utils import get_installer
from collective.js.galleria.testing import INTEGRATION_TESTING
from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles
from plone.registry.interfaces import IRegistry
from zope.component import getUtility

import unittest

PROJECTNAME = 'collective.js.galleria'
JS = '++resource++collective.galleria.js'


class InstallTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.registry = getUtility(IRegistry)
        self.qi_tool = get_installer(self.portal, self.request)

    def test_installed(self):
        self.assertTrue(
            self.qi_tool.is_product_installed(PROJECTNAME),
            'package appears not to have been installed',
        )

    def test_jsregistry(self):
        bundles = self.registry.collectionOfInterface(IBundleRegistry, prefix="plone.bundles")
        bundle = bundles['galleria']

        self.assertEqual(bundle.jscompilation,
            JS,
        )


class UninstallTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi_tool = get_installer(self.portal, self.request)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.qi_tool.uninstall_products(products=[PROJECTNAME])

    def test_uninstalled(self):
        self.assertFalse(self.qi.is_product_installed(PROJECTNAME))

    def test_jsregistry_removed(self):
        bundles = self.registry.collectionOfInterface(IBundleRegistry, prefix="plone.bundles")

        self.assertNotIn('galleria', bundles.keys())

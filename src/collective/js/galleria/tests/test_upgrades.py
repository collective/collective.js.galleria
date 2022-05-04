# -*- coding: utf-8 -*-
from collective.js.galleria.testing import INTEGRATION_TESTING
from datetime import datetime
from plone.app.testing import applyProfile
from plone.registry.interfaces import IRegistry
from Products.CMFPlone.interfaces import IBundleRegistry
from zope.component import getUtility

import unittest


class UpgradeTestCaseBase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self, from_version, to_version):
        self.portal = self.layer["portal"]
        self.setup = self.portal["portal_setup"]
        self.profile_id = "collective.js.galleria:default"
        self.from_version = from_version
        self.to_version = to_version

    def _get_upgrade_step(self, title):
        """Get one of the upgrade steps.

        Keyword arguments:
        title -- the title used to register the upgrade step
        """
        self.setup.setLastVersionForProfile(self.profile_id, self.from_version)
        upgrades = self.setup.listUpgrades(self.profile_id)
        steps = [s for s in upgrades[0] if s["title"] == title]
        return steps[0] if steps else None

    def _do_upgrade_step(self, step):
        """Execute an upgrade step.

        Keyword arguments:
        step -- the step we want to run
        """
        request = self.layer["request"]
        request.form["profile_id"] = self.profile_id
        request.form["upgrades"] = [step["id"]]
        self.setup.manage_doUpgrades(request=request)

    def _how_many_upgrades_to_do(self):
        self.setup.setLastVersionForProfile(self.profile_id, self.from_version)
        upgrades = self.setup.listUpgrades(self.profile_id)
        return len(upgrades[0])


class Upgrade1000to1001TestCase(UpgradeTestCaseBase):
    def setUp(self):
        UpgradeTestCaseBase.setUp(self, "1000", "1001")

    def test_registrations(self):
        version = self.setup.getLastVersionForProfile(self.profile_id)[0]
        self.assertGreaterEqual(int(version), int(self.to_version))
        self.assertEqual(self._how_many_upgrades_to_do(), 1)

    def test_update_bundle(self):
        title = "Update last_compilation and jscompilation of bundle"
        step = self._get_upgrade_step(title)
        self.assertIsNotNone(step)

        registry = getUtility(IRegistry)
        bundle = registry.forInterface(
            IBundleRegistry,
            prefix="plone.bundles/galleria.js",
        )

        # Simulate preview state.
        applyProfile(self.portal, "collective.js.galleria:1001-previous")

        self.assertEqual("++resource++collective.galleria.min.js", bundle.jscompilation)
        self.assertEqual(datetime(2021, 4, 3, 15, 0, 0, 5), bundle.last_compilation)

        self._do_upgrade_step(step)

        self.assertEqual(
            "++plone++collective.js.galleria/galleria.min.js", bundle.jscompilation
        )
        self.assertEqual(datetime(2022, 4, 29, 0, 0, 0, 4), bundle.last_compilation)

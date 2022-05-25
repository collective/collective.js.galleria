# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer


@implementer(INonInstallable)
class HiddenProfiles(object):
    def getNonInstallableProducts(self):
        """Hide the upgrades package from prefs_install_products_form."""
        return ["collective.js.galleria.upgrades"]

    def getNonInstallableProfiles(self):
        """Hide profiles from site-creation and quickinstaller."""
        return ["collective.js.galleria:uninstall"]


def post_install(context):
    """Post install script"""


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.

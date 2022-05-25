# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer


@implementer(INonInstallable)
class HiddenProfiles(object):
    def getNonInstallableProducts(self):
        """Hide tests profiles from prefs_install_products_form."""
        return ["collective.js.galleria.tests"]

    def getNonInstallableProfiles(self):
        """Hide profiles from site-creation and quickinstaller."""
        return []

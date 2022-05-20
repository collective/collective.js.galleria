# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing.zope import WSGI_SERVER
from zope.configuration import xmlconfig

import collective.js.galleria


class Fixture(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=collective.js.galleria)
        xmlconfig.file(
            "tests/configure.zcml", collective.js.galleria, context=configurationContext
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.js.galleria:default")


FIXTURE = Fixture()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name="collective.js.galleria:Integration",
)


FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE, WSGI_SERVER),
    name="collective.js.galleria:Functional",
)


COLLECTIVE_JS_GALLERIA_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        WSGI_SERVER,
    ),
    name="CollectiveJsGalleriaLayer:AcceptanceTesting",
)

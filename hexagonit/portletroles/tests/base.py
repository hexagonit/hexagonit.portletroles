from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer

import unittest2 as unittest


class HexagonitPortletrolesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""
        # Load ZCML
        import hexagonit.portletroles
        self.loadZCML(package=hexagonit.portletroles)
        self.loadZCML(package=hexagonit.portletroles, name="overrides.zcml")
        import hexagonit.portletroles.tests.rolemap
        self.loadZCML(package=hexagonit.portletroles.tests.rolemap)

    def setUpPloneSite(self, portal):
        """Set up Plone."""
        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'hexagonit.portletroles:default')
        self.applyProfile(portal, 'hexagonit.portletroles.tests.rolemap:default')

    def tearDownZope(self, app):
        """Tear down Zope."""


FIXTURE = HexagonitPortletrolesLayer()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name="HexagonitPortletrolesLayer:Integration")
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,), name="HexagonitPortletrolesLayer:Functional")


class IntegrationTestCase(unittest.TestCase):
    """Base class for integration tests."""

    layer = INTEGRATION_TESTING


class FunctionalTestCase(unittest.TestCase):
    """Base class for functional tests."""

    layer = FUNCTIONAL_TESTING

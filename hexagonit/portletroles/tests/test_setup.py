from hexagonit.portletroles.tests.base import IntegrationTestCase
from Products.CMFCore.utils import getToolByName


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = getToolByName(self.portal, 'portal_quickinstaller')

    def test_is_hexagonit_portletroles_installed(self):
        self.failUnless(self.installer.isProductInstalled('hexagonit.portletroles'))

    def test_registry(self):
        from plone.registry.interfaces import IRegistry
        from zope.component import getUtility
        registry = getUtility(IRegistry)
        portlets = registry['hexagonit.portletroles.portlets']
        self.assertEqual(
            len(registry['hexagonit.portletroles.portlets']),
            12
        )

    def test_uninstall__hexagonit_portletroles_not_installed(self):
        self.installer.uninstallProducts(['hexagonit.portletroles'])
        self.failIf(self.installer.isProductInstalled('hexagonit.portletroles'))

    def test_uninstall__hexagonit_portletroles_registry(self):
        self.installer.uninstallProducts(['hexagonit.portletroles'])
        from plone.registry.interfaces import IRegistry
        from zope.component import getUtility
        registry = getUtility(IRegistry)
        self.assertRaises(
            KeyError,
            lambda: registry['hexagonit.portletroles.portlets']
        )

    def test_browserlayer(self):
        from hexagonit.portletroles.browser.interfaces import IHexagonitPortletrolesLayer
        from plone.browserlayer import utils
        self.failUnless(IHexagonitPortletrolesLayer in utils.registered_layers())

from hexagonit.portletroles.tests.base import IntegrationTestCase
from Products.CMFCore.utils import getToolByName


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_is_hexagonit_portletroles_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('hexagonit.portletroles'))

    def test_uninstall__hexagonit_portletroles_not_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['hexagonit.portletroles'])
        self.failIf(installer.isProductInstalled('hexagonit.portletroles'))

    def test_browserlayer(self):
        from hexagonit.portletroles.browser.interfaces import IHexagonitPortletrolesLayer
        from plone.browserlayer import utils
        self.failUnless(IHexagonitPortletrolesLayer in utils.registered_layers())

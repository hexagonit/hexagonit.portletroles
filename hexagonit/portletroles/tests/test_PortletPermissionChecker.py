import mock
import unittest2 as unittest


class TestPortletPermissionChecker(unittest.TestCase):

    def createInstance(self):
        from hexagonit.portletroles.checker import PortletPermissionChecker
        context = mock.Mock()
        return PortletPermissionChecker(context)

    def test_instance(self):
        instance = self.createInstance()
        from hexagonit.portletroles.checker import PortletPermissionChecker
        self.assertTrue(isinstance(instance, PortletPermissionChecker))

    @mock.patch('hexagonit.portletroles.checker.getToolByName')
    @mock.patch('hexagonit.portletroles.checker.getSecurityManager')
    @mock.patch('hexagonit.portletroles.checker.aq_inner')
    def test__call_(self, aq_inner, getSecurityManager, getToolByName):
        instance = self.createInstance()
        aq_inner().REQUEST = {'ACTUAL_URL': '/portlets.Events'}
        getSecurityManager().checkPermission.return_value = True
        instance()
        getToolByName().checkPermission.assert_called_with(
            'Portlets: Manage Events portlets',
            aq_inner()
        )

    @mock.patch('hexagonit.portletroles.checker.getToolByName')
    @mock.patch('hexagonit.portletroles.checker.getSecurityManager')
    @mock.patch('hexagonit.portletroles.checker.aq_inner')
    def test__call_permission_false(self, aq_inner, getSecurityManager, getToolByName):
        instance = self.createInstance()
        aq_inner().REQUEST = {'ACTUAL_URL': '/portlets.Events'}
        getSecurityManager().checkPermission.return_value = True
        getToolByName().checkPermission.return_value = False
        from AccessControl import Unauthorized
        self.assertRaises(Unauthorized, lambda: instance())

    @mock.patch('hexagonit.portletroles.checker.getSecurityManager')
    @mock.patch('hexagonit.portletroles.checker.aq_inner')
    def test__call_not_a_portlet(self, aq_inner, getSecurityManager):
        instance = self.createInstance()
        aq_inner().REQUEST = {'ACTUAL_URL': '/not_a_portlet'}
        getSecurityManager().checkPermission.return_value = True
        instance()
        getSecurityManager().checkPermission.assert_called_with(
            'Portlets: Manage portlets',
            aq_inner()
        )

    @mock.patch('hexagonit.portletroles.checker.getSecurityManager')
    @mock.patch('hexagonit.portletroles.checker.aq_inner')
    def test__call_not_a_portlet_permission_false(self, aq_inner, getSecurityManager):
        instance = self.createInstance()
        aq_inner().REQUEST = {'ACTUAL_URL': '/not_a_portlet'}
        getSecurityManager().checkPermission.return_value = False
        from AccessControl import Unauthorized
        self.assertRaises(Unauthorized, lambda: instance())

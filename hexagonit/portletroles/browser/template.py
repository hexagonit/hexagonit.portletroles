from hexagonit.portletroles import _
from hexagonit.portletroles.portlet import Portlet
from hexagonit.portletroles.portlet import IPortlet
from plone.app.z3cform.layout import wrap_form
from plone.registry.interfaces import IRegistry
from plone.z3cform.crud import crud
from zope.component import getUtility
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class PortletRolesControlPanelForm(crud.CrudForm):

    update_schema = IPortlet

    label = _(u'Portlets and Permissions')

    def get_items(self):
        registry = getUtility(IRegistry)
        portlets = registry['hexagonit.portletroles.portlets']
        data = []
        for portlet in portlets:
            data.append(
                (
                    str(portlet['portlet']),
                    Portlet(
                        portlet['portlet'],
                        portlet['permission'],
                    )
                )
            )
        return data

    def add(self, data):
        """Add new portlet data to hexagonit.portletroles.portlets registry.

        :param data: Portlet data.
        :type data: dict
        """
        registry = getUtility(IRegistry)
        portlets = registry['hexagonit.portletroles.portlets']
        portlets.append(data)
        registry['hexagonit.portletroles.portlets'] = portlets

    def remove(self, (id, item)):
        """Delete portlet data from hexagonit.portletroles.portlets registry.

        :param id: Unique portlet name.
        :type id: str

        :param item: hexagonit.portletroles.portlet.Portlet instance.
        :type id: object
        """
        registry = getUtility(IRegistry)
        portlets = registry['hexagonit.portletroles.portlets']
        portlets = [portlet for portlet in portlets if portlet['portlet'] != id]
        registry['hexagonit.portletroles.portlets'] = portlets


PortletRolesControlPanelView = wrap_form(
    PortletRolesControlPanelForm,
    index=ViewPageTemplateFile('templates/controlpanel.pt')
)

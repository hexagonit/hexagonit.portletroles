from hexagonit.portletroles import _
from zope.interface import Interface
from zope.interface import implements
from zope.schema import Choice


class IPortlet(Interface):

    portlet = Choice(
        title=_(u'Portlet'),
        source="hexagonit.portletroles.Portlets",
    )
    permission = Choice(
        title=_(u'Permission'),
        source="hexagonit.portletroles.Permissions",
    )


class Portlet(object):

    implements(IPortlet)

    def __init__(
        self,
        # name,
        portlet,
        permission,

    ):
        self.portlet = portlet
        self.permission = permission

    def __repr__(self):
        return '<Bank with portlet={portlet!r, permission={permission!r}}'.format(
            portlet=self.portlet,
            permission=self.permission,

        )

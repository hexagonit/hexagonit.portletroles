from hexagonit.portletroles.config import PORTLETS
from plone.registry.interfaces import IRegistry
from zope.component import getUtility


def setupPortletRolesRegistry(context):
    registry = getUtility(IRegistry)
    if not registry['hexagonit.portletroles.portlets']:
        registry['hexagonit.portletroles.portlets'] = PORTLETS[:]
        log = context.getLogger(__name__)
        log.info('hexagonit.portletroles.portlets registry updated')


def setupVarious(context):

    if context.readDataFile(
        'hexagonit.portletroles_various.txt'
    ) is None:
        return

    setupPortletRolesRegistry(context)

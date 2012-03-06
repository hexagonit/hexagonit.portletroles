from plone.portlets.interfaces import IPortletManager
from zope.app.component.hooks import getSite
from zope.component import getUtility
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from plone.registry.interfaces import IRegistry


class PermissionsVocabulary(object):

    implements(IVocabularyFactory)

    def __call__(self, context):
        if hasattr(context, 'context'):
            portal = context.context
        elif getattr(getSite(), 'Type', None):
            portal = getSite()
        else:
            portal = getSite().context
        names = [
            item[
                'permission_name'
            ] for item in portal.manage_getPermissionMapping()
        ]
        items = [SimpleTerm(item, item, item) for item in names]
        return SimpleVocabulary(items)


PermissionsVocabularyFactory = PermissionsVocabulary()


class PortletsVocabulary(object):

    implements(IVocabularyFactory)

    def __call__(self, context):
        right = set(
            getUtility(IPortletManager, name=u"plone.rightcolumn").getAddablePortletTypes()
        )
        left = set(
            getUtility(IPortletManager, name=u"plone.leftcolumn").getAddablePortletTypes()
        )
        # registry = getUtility(IRegistry)
        # registered_portlets = [
        #     item['portlet'] for item in registry['hexagonit.portletroles.portlets']
        # ]
        # portlets = [
        #     item for item in list(
        #         right.union(left)
        #     ) if item.addview not in registered_portlets
        #     ]
        items = [
            SimpleTerm(
                item.addview,
                item.addview,
                item.title
            ) for item in list(right.union(left))
        ]
        return SimpleVocabulary(items)


PortletsVocabularyFactory = PortletsVocabulary()

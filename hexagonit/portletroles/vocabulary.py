from plone.portlets.interfaces import IPortletManager
from zope.app.component.hooks import getSite
from zope.component import getUtility
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


class PermissionsVocabulary(object):

    implements(IVocabularyFactory)

    def __call__(self, context):
        names = [
            item[
                'permission_name'
            ] for item in getSite().manage_getPermissionMapping()
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
        items = [
            SimpleTerm(
                item.addview,
                item.addview,
                item.title
            ) for item in list(right.union(left))
        ]
        return SimpleVocabulary(items)


PortletsVocabularyFactory = PortletsVocabulary()

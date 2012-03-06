from AccessControl import Unauthorized
from AccessControl import getSecurityManager
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from plone.app.portlets.interfaces import IPortletPermissionChecker
from plone.portlets.interfaces import IPortletAssignmentMapping
from plone.registry.interfaces import IRegistry
from zope.component import adapts
from zope.component import getUtility
from zope.interface import implements


# PERMISSIONS = {
#     'portlets.Events': 'Portlets: Manage Events portlets',
#     'plone.portlet.collection.Collection': 'plone.portlet.collection: Add collection portlet',
#     'portlets.Login': 'Portlets: Manage Login portlets',
#     'portlets.Navigation': 'Portlets: Manage Navigation portlets',
#     'collective.quickupload.QuickUploadPortlet': 'Portlets: Manage QuickUpload portlets',
#     'portlets.rss': 'Portlets: Manage RSS portlets',
#     'portlets.Recent': 'Portlets: Manage Recent portlets',
#     'portlets.Review': 'Portlets: Manage Review portlets',
#     'portlets.Search': 'Portlets: Manage Search portlets',
#     'plone.portlet.static.Static': 'plone.portlet.static: Add static portlet',
# }


# class PortletPermissionChecker(object):
#     implements(IPortletPermissionChecker)
#     adapts(IPortletAssignmentMapping)

#     def __init__(self, context):
#         self.context = context

def __call__(self):
    sm = getSecurityManager()
    context = aq_inner(self.context)
    portlet = context.REQUEST.get('ACTUAL_URL').split('/')[-1]
    registry = getUtility(IRegistry)
    portlets = [
        {
            item['portlet']: item['permission']

        } for item in registry['hexagonit.portletroles.portlets']
    ]
    if portlet not in portlets:
        if not sm.checkPermission("Portlets: Manage portlets", context):
            raise Unauthorized("You are not allowed to manage portlets")
        ## Should we check portlets dependent permissions here too...?
        return
    permission = portlets[portlet]
    mtool = getToolByName(context, 'portal_membership')
    if not mtool.checkPermission(permission, context):
        raise Unauthorized("You are not allowed to manage portlets")

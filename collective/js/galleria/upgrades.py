from Products.CMFCore.utils import getToolByName

def cookResources(context):
    jsregistry = getToolByName(context, 'portal_javascripts')
    jsregistry.cookResources()

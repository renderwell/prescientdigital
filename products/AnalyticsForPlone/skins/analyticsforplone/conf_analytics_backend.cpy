##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters = uacct, filter_analytics=False, filter_on_view=True, filter_on_templates=[]
##title=Configure Analytics for Plone
##

req = context.REQUEST

tool = context.analytics_tool

# Clean value before storing them into properties
uacct = uacct.strip()
filter_on_templates = [x.strip() for x in filter_on_templates
                       if x]

tool.manage_changeProperties(uacct=uacct, filter_analytics=filter_analytics,
    filter_on_view=filter_on_view, filter_on_templates=filter_on_templates,)

return state.set(status="success", portal_status_message="Analytics for Plone succesfully updated.")

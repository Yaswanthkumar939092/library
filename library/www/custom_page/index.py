from frappe import _

def get_context(context):
    context.aaaa = _('Custom Page')
    context.message = 'This is a custom page created using Frappe.'
    # Add any additional context variables or logic here
    return context

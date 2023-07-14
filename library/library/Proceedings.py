import frappe
from frappe import get_doc, new_doc
@frappe.whitelist(allow_guest=True)



# def check():
#       new_items = frappe.get_doc({
#         "doctype": "Proceedings",
#         "case_type": "hello",
#         "property_right": "PR-00001",
#         "jurisdiction":"JU-00001",
#         "proceedings_name":"RAVI",

#         "items": [
#             {
#                 "field": "Or",
                
#             }
#         ]
#     })
#     #   new_items.insert(ignore_permissions=True)
#       new_items.save()

def get_details(name1=None):
    print(frappe.db.sql("""SELECT name1 FROM `tabBanana`;""",as_dict=True))
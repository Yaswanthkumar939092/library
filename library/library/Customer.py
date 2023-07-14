
import frappe
from frappe.model.document import Document
# def create():
#     doc = get_doc({
#     'doctype': 'Customer',
#     'customer_name':"Nag",
#     'customer_type':'Company',
#     'customer_group':'All Customer Groups',
#     'territory':"All Territories"
#    })
#     doc.insert()

# def is_available():
#         if frappe.db.exists("Customer",'Lavaraju'):
#             doc = frappe.get_doc("Lavaraju")
#             for d in doc:
#                  frappe.msgprint("The customer Name {0} and customer type is {1}".format(d.customer_name,d.customer_type))
#         else:
#              frappe.msgprint("The Document Name is Not Exists in the Data base")

def is_available(customer_id):
      if frappe.db.exists("Customer",customer_id):
        doc = frappe.db.get_list("Customer",fields = ["customer_name",'customer_type'])
        for d in doc:
            if d.customer_name==customer_id:
                print("The customer Name {0} and customer type is {1}".format(d.customer_name,d.customer_type))
            # else:
                # print("sdfghj")

def test():
    is_available(customer_id = "Yashwanth")

# def modify_customer():
#     frappe.db.set_value('Customer','Nag',{
#         'customer_type':"Individual",
#         'customer_group':'Individual'
#     })

# def delete_customer():
#     frappe.delete_doc('Customer',"Lavaraju")
# import frappe
# from frappe import get_doc, new_doc
import frappe
# from frappe.model.document import Document
from frappe import get_doc, new_doc
@frappe.whitelist(allow_guest=True)

# def check(Quotation):
#       if frappe.db.exists("Customer",Quotation):
#         doc = frappe.db.get_list("Customer",fields = ["customer_name"])
#         for d in doc:
#             if d.customer_name==Quotation:
#                 print("The customer Name {0}".format(d.customer_name))
#             else :
#                 print("Customer is not available")

def include():
    doc=frappe.get_doc("Customer","Raju")
    doc.title='Test'
    doc.save()
    # check(Quotation = "Raju")

    # sales_order = frappe.get_doc({
    #     "doctype": "Quotation",
    #     "quotation_to": "Customer",
    #     "transaction_date": "2013-02-23",
    #     "items": [
    #         {
    #             "item_code": "ITM-001",
    #             "qty": 10.0,
    #         }
    #     ]
    # })
    # sales_order.insert(ignore_permissions=True)
    # sales_order.save()



# def test():
#     doc = frappe.new_doc('Quotation')
#     doc.Date = 12/12/2002,
#     doc.Customer="Raju"
#     doc.insert()

# def create_quotation(customer, items):
#     # Create a new Quotation document
#     quotation = new_doc("Quotation")
    
#     # Set the customer
#     quotation.customer = customer
    
#     # Add items to the quotation
#     for item in items:
#         quotation.append("items", {
#             "Quotation To": item["Quotation To"],
#             "Date": item["Date"],
#             "Order Type": item["Order Type"],
#             "Customer":item["Customer"],
#             # "Item_code":item["Item_code"],
#             # "Quantity":item["Quantity"]
#         })
    
#     # Save the quotation document
#     quotation.insert()
    
#     return quotation.name  # Return the name of the created quotation

# # Example usage
# customer = "Raju"
# items = [
#     {"Quotation To": "Kamal", "Date":"2/3/2020", "Order Type": "Sales", "Customer":"Raju"},
# ]

# quotation_name = create_quotation(customer, items)
# print("Quotation created with name:", quotation_name)
# # 
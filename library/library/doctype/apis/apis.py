# Copyright (c) 2023, Yashwanth kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Apis(Document):
	pass

@frappe.whitelist(allow_guest=True)
def get_apis(name1=None, age=None):
    if frappe.local.request.method=="GET":
        data=frappe.db.get_list('Apis',
        fields=['name1','age'],
        ignore_permissions=True)
        if name1!=None:
            data=frappe.db.get_list('Apis',
            filters={'name1':name1},
            fields=['name1','age'],
            ignore_permissions=True)
            return data
        return data
    if frappe.local.request.method=='POST':
        doc=frappe.new_doc('Apis')
        doc.name1=name1
        doc.age=age
        doc.insert(ignore_permissions=True)
        doc.save()
        return doc
    if frappe.local.request.method == 'PUT':
         doc=frappe.get_doc('Apis','06')
         doc.name1=name1
         doc.age=age
         doc.save(ignore_permissions=True)
         return doc
    if frappe.local.request.method == 'DELETE':
         doc=frappe.get_doc('Apis','06')
         doc.delete(ignore_permissions=True)
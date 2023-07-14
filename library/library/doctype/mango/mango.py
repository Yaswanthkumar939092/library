# Copyright (c) 2023, Yashwanth kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Mango(Document):
	pass

from frappe import get_doc

def add_custom_field():
	doc = get_doc("DocType","Mango")
	doc.append('fields',{
		'label':'Full Name',
		'fieldname':'full_name',
		'fieldtype':'Data',
		'insert_after':"roll_no",
		#'depends_on':'eval:doc.field_name',
		'reqd':1
	})
	doc.save()
# Copyright (c) 2023, Yashwanth kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Sai(Document):
    pass
	# frappe.db.delete_doc('Task', 'TASK00004')
def aa():
    frappe.db.rename_table("Sai", "SaiKumar")
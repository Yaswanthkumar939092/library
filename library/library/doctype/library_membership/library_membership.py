# Copyright (c) 2023, Yashwanth kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus


class LibraryMembership(Document):
    pass
    # frappe.db.delete_doc('Task', 'TASK00004')

	# def before_submit(self):

		

	# 	if self.to_date < self.from_date:
	# 		frappe.msgprint("There is an active membership for this member")
	# 	else:
	# 		frappe.msgprint('There is no active membership for this member')
  
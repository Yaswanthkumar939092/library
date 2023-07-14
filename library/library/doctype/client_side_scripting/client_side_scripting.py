# Copyright (c) 2023, Yashwanth kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class client_side_scripting(Document):
	pass

@frappe.whitelist()
def frappe_call(msg):
	import time
	time.sleep(5)
	frappe.msgprint(msg)

	# return "Hi Message from frappe_call"
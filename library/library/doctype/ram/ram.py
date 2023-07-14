# Copyright (c) 2023, Yashwanth kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Ram(Document):
		pass
def bb():
	frappe.db.get_single_value('Ram', 'Date')


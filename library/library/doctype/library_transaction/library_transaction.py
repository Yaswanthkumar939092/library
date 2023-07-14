# Copyright (c) 2023, Yashwanth kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus


class LibraryTransaction(Document):
	def before_submit(self):
              if self.type == "issue":
                     frappe.msgprint("App Isssued")
                    #   self.validate_issue()
                    #   article = frappe.get_doc("Article", self.article)
                    #   article.status = "Issued"
                    #   article.save()
					# frappe.msgprint("App Isssued")
              elif self.type == "return":
                     frappe.msgprint("App returned")
                    #   self.validate_return()
                    #   article = frappe.get_doc("Article", self.article)
                    #   article.status = "Available"
                    #   article.save()


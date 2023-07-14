# Copyright (c) 2023, Yashwanth kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class YashwanthKumar(Document):
	pass




	# def before_insert(doc, method):
		# doc.some_field = "Default Value"

	# def get_doc_before_save(self):
        # # Perform custom actions or validations here
		# if self.name1 == self.description:
		# 	frappe.throw(("Field 1 and Field 2 cannot be the same."))

        # # Example: Set a timestamp field before saving
		# self.timestamp_field = frappe.utils.now()

        # # Call the parent's get_doc_before_save() method
		# super(YashwanthKumar, self).get_doc_before_save()

# def aa():
# 	doc=frappe.new_doc("Employee")

# 	def before_insert(doc, method):
# 		doc.employee_code = generate_employee_code(method)

# def generate_employee_code(method):
#     last_employee_code = method.get("last_employee_code") or "EMP000"
#     # Logic to generate a unique employee code based on the last code
#     employee_code = "EMP" + str(int(last_employee_code[3:]) + 1).zfill(3)
#     method.last_employee_code = employee_code
#     return employee_code

# 	doc.name1="Kamal"
# 	doc.diescription="Sinior Developer"
# 	doc.status="open"
# 	doc.insert()

	# print(frappe.db.exists({"doctype": "YashwanthKumar", "name": "ad50de0bcc"}))

	# pass
	# print(frappe.db.rename_table("HINDI", "YashwanthKumar"))


	# frappe.delete_doc('YashwanthKumar', 'Baby01')

	# frappe.rename_doc('YashwanthKumar', 'Lava09', 'Baby01')

	# doc = frappe.get_doc('YashwanthKumar','Lava07')
	# doc.title = 'Test'
	# doc.save()
	# pass
	# frappe.db.truncate("YashwanthKumar")


	# doc=frappe.new_doc("YashwanthKumar")
	# doc.name1="Hyde234"
	# doc.diescription="Lover Boy"
	# doc.status="open"
	# doc.insert()
	# print(frappe.db.exists({"doctype": "YashwanthKumar", "name": "ad50de0bcc"}))

	# print(frappe.db.get_single_value('System Settings', 'time_zone'))

	# print(frappe.db.get_single_value(YashwanthKumar, 'hello'))


	# print(frappe.db.set_value('YashwanthKumar', 'de-1234', 'name', 'Hey'))

# 	print(frappe.db.get_list('YashwanthKumar', filters=[[
#     'date', 'between', ['2023-06-21', '2023-06-30']
# ]]))

	# print(frappe.db.get_list('YashwanthKumar',
    # filters={
    #     'status': 'close'
    # },
    # fields=['name', 'date'],))
	# print(frappe.db.get_list('YashwanthKumar',
    # fields=['count(name) as count', 'status'],
    # group_by='status'))
	# print(frappe.db.count('YashwanthKumar'))
	# print(frappe.db.count('YashwanthKumar', {'status': 'close'}))
	# print(frappe.db.get_all('YashwanthKumar'))

	
	# timezone = frappe.db.get_single_value('YashwanthKumar', 'Date')

	# frappe.db.change_column_type(Sai, column, text)


		# print(frappe.db.get_value('Sai','Task00012','description'))
		# frappe.db.rename_table("Sai", "SaiKumar")

# @frappe.whitelist(allow_guest=True)
# def get_details(name1=None):
#     return(frappe.db.sql("""SELECT name1 FROM `tabBanana` WHERE emp_type='intern';""",as_list=True))
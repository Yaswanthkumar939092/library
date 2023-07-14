# Copyright (c) 2023, Yashwanth kumar and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = [], []
	# return columns, data
	columns = [
        {
            'fieldname': 'name1',
            'label': 'Name',
            'fieldtype': 'Data',
            'options': 'Name'
        },
        {
            'fieldname': 'description',
            'label': 'description',
            'fieldtype': 'Data',
            'options': 'description'
        },
        {
            'fieldname': 'status',
            'label':'status',
            'fieldtype': 'Select',
            'options': 'open'
        }
    ]
	data = frappe.db.sql("""
	select
		name1,description,status
	from
		`tabYashwanthKumar`""")
	return columns, data
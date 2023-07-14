# Copyright (c) 2023, Yashwanth kumar and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = [], []
	columns = [
        {
            'fieldname': 'name1',
            'label': 'Name',
            'fieldtype': 'Data',
            'options': 'Name'
        },
        {
            'fieldname': 'roll_no',
            'label': 'Roll_No',
            'fieldtype': 'int',
            'options': 'Roll_No'
        },
        # {
        #     'fieldname': 'emp_type',
        #     'label':'Emp_Type',
        #     'fieldtype': 'Select',
        #     'options': 'intern'
        # },
	
    ]
	data = frappe.db.sql("""
		select
			name1,roll_no,
				from
			`tabMango`""")
	return columns, data
# Copyright (c) 2023, Yashwanth kumar and contributors
# For license information, please see license.txt

# import frappe


def execute(filters=None):
	columns, data = [], []
	columns = [
        {
            'fieldname': 'name',
            'label': 'Name',
            'fieldtype': 'data',
        }
    ]

	return columns, data

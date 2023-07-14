# Copyright (c) 2023, Yashwanth kumar and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = [], []
	columns = [
        {
            'fieldname': 'account',
            'label': 'Accohjvunt',
            'fieldtype': 'Link',
            'options': 'Account'
        },
        {
            'fieldname': 'currency',
            'label': 'Currency',
            'fieldtype': 'Link',
            'options': 'Currency'
        },
        {
            'fieldname': 'balance',
            'label':'Balance',
            'fieldtype': 'Currency',
            'options': 'currency'
        }
    ]
	data = frappe.db.sql("""
	select
		account,debit_in_account_currency,account
	from
		`tabGL Entry`""")
	return columns, data

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
            'fieldtype': 'Int',
            'options': 'Roll_No'
        },
        {
            'fieldname': 'emp_type',
            'label': 'Emp_Type',
            'fieldtype': 'Select',
            'options': 'Emp_Type'
        },
    ]
    
    name_filter = ""
    # rollno_filter=""
    if filters and filters.get('name'):
        name_filter = "AND m.name1 = '{0}'".format(filters['name'])
        # rollno_filter="AND m.roll_no='{0}'".format(filters['roll_no'])
    
    data = frappe.db.sql("""SELECT m.name1, m.roll_no, b.emp_type
                           FROM `tabMango` m
                           JOIN `tabBanana` b ON m.name1 = b.name1
                           WHERE 1=1 {0}""".format(name_filter))
    
    return columns, data


# def execute(filters=None):
# 	columns, data = [], []
# 	columns = [
#         {
#             'fieldname': 'name1',
#             'label': 'Name',
#             'fieldtype': 'Data',
#             'options': 'Name'
#         },
#         {
#             'fieldname': 'roll_no',
#             'label': 'Roll_No',
#             'fieldtype': 'int',
#             'options': 'Roll_No'
#         },
# 	{
# 		'fieldname':'emp_type',
# 		'label':'Emp_Type',
# 		'fieldtype':'Select',
# 		'options':'Emp_Type'
#     },
# 	]
# 	data = frappe.db.sql("""SELECT m.name1, m.roll_no, b.emp_type
#                FROM `tabMango` m
#                JOIN `tabBanana` b ON m.name1 = b.name1
# 	       """)
# 	return columns, data

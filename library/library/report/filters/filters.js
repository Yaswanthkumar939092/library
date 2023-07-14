// Copyright (c) 2023, Yashwanth kumar and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Filters"] = {
	"filters": [
		{
            fieldname: 'Customer',
            label: __('Customer'),
            fieldtype: 'Link',
            options: 'Customer',
        }
	]
};

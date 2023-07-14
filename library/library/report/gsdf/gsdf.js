// Copyright (c) 2023, Yashwanth kumar and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Gsdf"] = {
	"filters": [
		{
            fieldname: 'company',
            label: __('Company'),
            fieldtype: 'Link',
            options: 'Company',
        }
	]
};

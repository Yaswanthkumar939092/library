// Copyright (c) 2023, Yashwanth kumar and contributors
// For license information, please see license.txt

frappe.ui.form.on('server_side_scripting', {
	enable: function(frm){
		frappe.call({
			method:'library.library.doctype.client_side_scripting.client_side_scripting.frappe_call',
			args:{
				msg:'Hello'
			},
			freeze:true,
			freeze_message:_('Calling frappe_call Method'),
			callback:function(r){
				frappe.msgprint(r.message)
			}
		})
	}
});

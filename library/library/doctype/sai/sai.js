// Copyright (c) 2023, Yashwanth kumar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Sai', {
	on_submit: function(frm){
		frappe.msgprint("Hello this is on submit event")
	}
});
// onload: function(frm) {
// 	frappe.msgprint("Hello this is onload")
// 	console.log(frm)
// }

// before_save: function(frm){
// 	frappe.throw("Hellow this is before save event ")
// }


// enable: function(frm) {
// 	frappe.msgprint("Hello thi is enable event")
// },
// age: function(frm) {
// 	frappe.msgprint("hello this is age event")
// },

// before_submit: function(frm){
// 	frappe.throw("Hello this is before submit event")
// }

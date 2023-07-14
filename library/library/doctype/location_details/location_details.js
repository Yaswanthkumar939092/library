// Copyright (c) 2023, Yashwanth kumar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Location Details', {
		map: function(frm) {
			let mapData = JSON.parse(frm.doc.geolocation).features[0];
			if (mapData && mapData.geometry.type=='Point') {
				let lat = mapData.geometry.coordinates[1];
				let lon = mapData.geometry.coordinates[0];
				frappe.call({
					type : "GET",
					url:`https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lon}`, //dotted path to server method
					callback: function(data) {
						
						// console.log(data.display_name)
						frm.set_value("address",data.address)
					}
				});
				
				
			}
		}
		
});

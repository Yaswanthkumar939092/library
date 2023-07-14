frappe.query_reports["Hello"] = {
    "filters": [
        {
            fieldname: 'name',
            label: __('Name'),
            fieldtype: 'Data',
            options: 'Name',
        },
    ],
    "onload": function(report) {
        // Define the filter change event handler
        report.events.on('filtersChange', function() {
            // Get the current filter values
            var filters = report.getValues();
            var name = filters.name;
            var roll_no=filters.roll_no;
            
            // Perform any additional logic or actions based on the filter values
            // ...
            
            // Refresh the report data
            report.refresh();
        });
    }
};

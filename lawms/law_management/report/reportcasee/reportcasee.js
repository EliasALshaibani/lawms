// Copyright (c) 2024, elias Alshaibani and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["reportcasee"] = {
	"filters": [
 
        {
            "fieldname": "case_status",
            "label": __("Case Status"),
            "fieldtype": "Select",
            "options": "\nOpen\nClosed\nPending",
            "default": "Open"
        },
        {
            "fieldname": "client",
            "label": __("Client"),
            "fieldtype": "Link",
            "options": "Clients",
            "default": ""
        },
        {
            "fieldname": "session_date_from",
            "label": __("Session Date From"),
            "fieldtype": "Date",
            "default": frappe.datetime.get_today(),
        },
        {
            "fieldname": "session_date_to",
            "label": __("Session Date To"),
            "fieldtype": "Date",
        }

	]
};

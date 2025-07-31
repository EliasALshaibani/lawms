// Copyright (c) 2024, elias Alshaibani and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["reportSessionss"] = {
	"filters": [
           {fieldname:"case_subject",label:_("case_subject"),fieldtype:"Link",options:"Casee",default:frappe.defaults.get_user_default("case_subject"),reqd:1},
           {fieldname:"gregorian_date",label:_("Session Date"),fieldtype:"Date",default:frappe.defaults.get_user_default("year_start_date")},

	]
};

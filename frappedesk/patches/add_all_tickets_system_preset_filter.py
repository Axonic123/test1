import frappe


def execute():
	preset_filter_doc = frappe.get_doc(
		{
			"doctype": "FD Preset Filter",
			"title": "All Tickets",
			"reference_doctype": "Ticket",
			"filters": [],
		}
	)
	preset_filter_doc.insert()

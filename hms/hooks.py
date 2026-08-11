app_name = "hms"
app_title = "Hospital Management System"
app_publisher = "sagarmemane135"
app_description = "Frappe v16 Hospital & Patient Management System"
app_email = "wjones13522@gmail.com"
app_license = "mit"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/hms/css/hms.css"
# app_include_js = "/assets/hms/js/hms.js"

# Desktop Notifications & Workspaces
# -----------------------------------
has_website_permission = "hms.patient_management.doctype.patient.patient.has_website_permission"

# DocType Events
# ---------------
# Hook on document events for automated workflows (e.g., bed status update on admission/discharge)
doc_events = {
	"Bed Allocation": {
		"on_submit": "hms.ipd_management.doctype.bed_allocation.bed_allocation.update_bed_status",
		"on_cancel": "hms.ipd_management.doctype.bed_allocation.bed_allocation.release_bed_status"
	}
}

# Scheduled Tasks
# ---------------
# scheduler_events = {
# 	"daily": [
# 		"hms.tasks.daily_bed_occupancy_report"
# 	]
# }

# Fixtures
# --------
# fixtures = ["Custom Field", "Property Setter"]

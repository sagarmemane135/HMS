import frappe
from frappe.model.document import Document

class BedAllocation(Document):
	def on_submit(self):
		update_bed_status(self, method="on_submit")

	def on_cancel(self):
		release_bed_status(self, method="on_cancel")

def update_bed_status(doc, method=None):
	if doc.bed:
		frappe.db.set_value("Bed", doc.bed, {
			"status": "Occupied",
			"current_patient": doc.patient
		})

def release_bed_status(doc, method=None):
	if doc.bed:
		frappe.db.set_value("Bed", doc.bed, {
			"status": "Available",
			"current_patient": None
		})

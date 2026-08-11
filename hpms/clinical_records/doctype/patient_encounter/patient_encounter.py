import frappe
from frappe.model.document import Document

class PatientEncounter(Document):
	def on_submit(self):
		self.status = "Completed"
		if self.appointment:
			frappe.db.set_value("Patient Appointment", self.appointment, "status", "Completed")

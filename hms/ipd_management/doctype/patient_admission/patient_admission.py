import frappe
from frappe.model.document import Document

class PatientAdmission(Document):
	def on_submit(self):
		frappe.db.set_value("Patient", self.patient, "status", "Admitted")
		if self.assigned_bed:
			# Auto create Bed Allocation record
			alloc = frappe.get_doc({
				"doctype": "Bed Allocation",
				"patient": self.patient,
				"patient_admission": self.name,
				"bed": self.assigned_bed,
				"allocation_date": self.admission_datetime,
				"status": "Active"
			})
			alloc.insert(ignore_permissions=True)
			alloc.submit()

	def on_cancel(self):
		frappe.db.set_value("Patient", self.patient, "status", "Active")

import frappe
from frappe.model.document import Document

class DischargeSummary(Document):
	def on_submit(self):
		if self.patient_admission:
			frappe.db.set_value("Patient Admission", self.patient_admission, "status", "Discharged")
		
		frappe.db.set_value("Patient", self.patient, "status", "Discharged")
		
		# Release active bed allocation
		allocations = frappe.get_all("Bed Allocation", filters={"patient_admission": self.patient_admission, "docstatus": 1, "status": "Active"})
		for alloc_item in allocations:
			alloc_doc = frappe.get_doc("Bed Allocation", alloc_item.name)
			alloc_doc.status = "Released"
			alloc_doc.release_date = self.discharge_date
			alloc_doc.save(ignore_permissions=True)
			if alloc_doc.bed:
				frappe.db.set_value("Bed", alloc_doc.bed, {"status": "Cleaning", "current_patient": None})

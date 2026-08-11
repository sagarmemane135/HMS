import frappe
from frappe.model.document import Document

class PatientAppointment(Document):
	def validate(self):
		if not self.consultation_fee and self.doctor:
			self.consultation_fee = frappe.db.get_value("Doctor", self.doctor, "consultation_fee") or 0.0

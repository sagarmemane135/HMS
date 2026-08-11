import frappe
from frappe.model.document import Document

class Patient(Document):
	def validate(self):
		if self.patient_name:
			self.patient_name = self.patient_name.strip()

def has_website_permission(doc, ptype, user=None):
	if not user:
		user = frappe.session.user
	if "System Manager" in frappe.get_roles(user) or "Doctor" in frappe.get_roles(user):
		return True
	patient = frappe.db.get_value("Patient", {"email": user}, "name")
	return doc.name == patient

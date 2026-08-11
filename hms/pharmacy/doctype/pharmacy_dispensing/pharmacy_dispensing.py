import frappe
from frappe.model.document import Document

class PharmacyDispensing(Document):
	def on_submit(self):
		self.status = "Dispensed"

import frappe
from frappe.model.document import Document

class LabResult(Document):
	def on_submit(self):
		if self.lab_order:
			frappe.db.set_value("Lab Order", self.lab_order, "status", "Completed")

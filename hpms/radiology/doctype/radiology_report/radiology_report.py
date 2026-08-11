import frappe
from frappe.model.document import Document

class RadiologyReport(Document):
	def on_submit(self):
		if self.imaging_order:
			frappe.db.set_value("Imaging Order", self.imaging_order, "status", "Completed")

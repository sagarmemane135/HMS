import frappe
from frappe.model.document import Document

class PatientInvoice(Document):
	def validate(self):
		self.grand_total = (self.consultation_charge or 0) + (self.bed_charge or 0) + (self.lab_charge or 0) + (self.radiology_charge or 0) + (self.pharmacy_charge or 0)
		self.outstanding_amount = self.grand_total - (self.paid_amount or 0)
		
		if self.outstanding_amount <= 0 and self.grand_total > 0:
			self.status = "Paid"
		elif self.paid_amount and self.paid_amount > 0:
			self.status = "Partially Paid"
		else:
			self.status = "Unpaid"

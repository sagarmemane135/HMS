import frappe
from frappe.model.document import Document

class VitalSigns(Document):
	def validate(self):
		self.calculate_bmi()

	def calculate_bmi(self):
		if self.height_cm and self.weight_kg and self.height_cm > 0:
			height_m = self.height_cm / 100.0
			self.bmi = round(self.weight_kg / (height_m * height_m), 2)

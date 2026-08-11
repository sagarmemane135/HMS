frappe.ui.form.on('Patient Invoice', {
	consultation_charge(frm) { frm.trigger('calculate_total'); },
	bed_charge(frm) { frm.trigger('calculate_total'); },
	lab_charge(frm) { frm.trigger('calculate_total'); },
	radiology_charge(frm) { frm.trigger('calculate_total'); },
	pharmacy_charge(frm) { frm.trigger('calculate_total'); },
	paid_amount(frm) { frm.trigger('calculate_total'); },
	calculate_total(frm) {
		let total = (frm.doc.consultation_charge || 0) + 
					(frm.doc.bed_charge || 0) + 
					(frm.doc.lab_charge || 0) + 
					(frm.doc.radiology_charge || 0) + 
					(frm.doc.pharmacy_charge || 0);
		frm.set_value('grand_total', total);
		frm.set_value('outstanding_amount', total - (frm.doc.paid_amount || 0));
	}
});

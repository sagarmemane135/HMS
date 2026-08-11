frappe.ui.form.on('Patient Admission', {
	refresh(frm) {
		if (frm.doc.docstatus === 1 && frm.doc.status === 'Admitted') {
			frm.add_custom_button(__('Discharge Patient'), function() {
				frappe.new_doc('Discharge Summary', {
					patient: frm.doc.patient,
					patient_admission: frm.doc.name,
					discharge_date: frappe.datetime.now_datetime()
				});
			});
		}
	}
});

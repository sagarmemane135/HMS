frappe.ui.form.on('Patient', {
	refresh(frm) {
		if (!frm.is_new()) {
			frm.add_custom_button(__('Book Appointment'), function() {
				frappe.new_doc('Patient Appointment', {
					patient: frm.doc.name,
					patient_name: frm.doc.patient_name
				});
			}, __('Actions'));

			frm.add_custom_button(__('New Encounter'), function() {
				frappe.new_doc('Patient Encounter', {
					patient: frm.doc.name
				});
			}, __('Actions'));
		}
	}
});

frappe.ui.form.on('Patient Encounter', {
	refresh(frm) {
		if (!frm.is_new()) {
			frm.add_custom_button(__('Record Vitals'), function() {
				frappe.new_doc('Vital Signs', {
					patient: frm.doc.patient
				});
			}, __('Orders'));

			frm.add_custom_button(__('Order Lab Test'), function() {
				frappe.new_doc('Lab Order', {
					patient: frm.doc.patient,
					doctor: frm.doc.doctor,
					patient_encounter: frm.doc.name
				});
			}, __('Orders'));

			frm.add_custom_button(__('Order Radiology'), function() {
				frappe.new_doc('Imaging Order', {
					patient: frm.doc.patient,
					doctor: frm.doc.doctor,
					patient_encounter: frm.doc.name
				});
			}, __('Orders'));
		}
	}
});

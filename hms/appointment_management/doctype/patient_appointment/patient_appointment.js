frappe.ui.form.on('Patient Appointment', {
	refresh(frm) {
		if (frm.doc.status === 'Checked In' || frm.doc.status === 'Waiting') {
			frm.add_custom_button(__('Start Encounter'), function() {
				frappe.new_doc('Patient Encounter', {
					patient: frm.doc.patient,
					doctor: frm.doc.doctor,
					appointment: frm.doc.name
				});
			});
		}
	}
});

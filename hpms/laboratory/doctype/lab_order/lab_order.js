frappe.ui.form.on('Lab Order', {
	refresh(frm) {
		if (frm.doc.docstatus === 1 && frm.doc.status !== 'Completed') {
			frm.add_custom_button(__('Enter Test Result'), function() {
				frappe.new_doc('Lab Result', {
					patient: frm.doc.patient,
					lab_order: frm.doc.name,
					lab_test: frm.doc.lab_test
				});
			});
		}
	}
});

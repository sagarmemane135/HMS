frappe.ui.form.on('Imaging Order', {
	refresh(frm) {
		if (frm.doc.docstatus === 1 && frm.doc.status !== 'Completed') {
			frm.add_custom_button(__('Create Radiology Report'), function() {
				frappe.new_doc('Radiology Report', {
					patient: frm.doc.patient,
					imaging_order: frm.doc.name,
					modality: frm.doc.modality
				});
			});
		}
	}
});

frappe.ui.form.on('Vital Signs', {
	height_cm(frm) {
		frm.trigger('calculate_bmi');
	},
	weight_kg(frm) {
		frm.trigger('calculate_bmi');
	},
	calculate_bmi(frm) {
		if (frm.doc.height_cm && frm.doc.weight_kg && frm.doc.height_cm > 0) {
			let height_m = frm.doc.height_cm / 100.0;
			let bmi = (frm.doc.weight_kg / (height_m * height_m)).toFixed(2);
			frm.set_value('bmi', parseFloat(bmi));
		}
	}
});

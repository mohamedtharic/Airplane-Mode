// Copyright (c) 2026, Tharic and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airport Shop", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Airport Shop', {
    onload(frm) {
        frm.set_query("shop_type", function() {
            return {
                filters: {
                    enabled: 1
                }
            };
        });
    }
});

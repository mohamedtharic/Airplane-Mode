frappe.ui.form.on('Airline', {
    refresh: function(frm) {

        // check if website field has value
        if (frm.doc.website) {

            // add clickable website link in form header
            frm.add_web_link(frm.doc.website, "Website");

        }

    }
});

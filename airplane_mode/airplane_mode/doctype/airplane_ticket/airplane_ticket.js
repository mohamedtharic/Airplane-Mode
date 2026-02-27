frappe.ui.form.on('Airplane Ticket', {
    refresh(frm) {

        // add button only when doc is saved (not new)
        if (!frm.is_new()) {

            frm.add_custom_button('Assign Seat', () => {

                let d = new frappe.ui.Dialog({
                    title: 'Assign Seat',
                    fields: [
                        {
                            label: 'Seat Number',
                            fieldname: 'seat',
                            fieldtype: 'Data',
                            reqd: 1
                        }
                    ],
                    primary_action_label: 'Assign',
                    primary_action(values) {

                        // set seat field in form
                        frm.set_value('seat', values.seat);

                        d.hide();
                    }
                });

                d.show();
            });

        }
    }
});

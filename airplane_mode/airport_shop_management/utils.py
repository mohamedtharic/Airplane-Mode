import frappe

def send_rent_reminders():
    settings = frappe.get_single("Shop Settings")

    if not settings.enable_rent_remainder:
        return

    contracts = frappe.get_all(
        "Shop Lease Contract",
        fields=["tenant", "rent_amount"]
    )

    for c in contracts:

        tenant_email = frappe.db.get_value(
            "Shop Tenant",
            c.tenant,
            "email"
        )

        if tenant_email:
            frappe.sendmail(
                recipients=tenant_email,
                subject="Monthly Rent Reminder",
                message=f"Your monthly rent of {c.rent_amount} is due."
            )

def update_ticket_gates(flight, gate):

    tickets = frappe.get_all(
        "Airplane Ticket",
        filters={"flight": flight},
        pluck="name"
    )

    for t in tickets:
        frappe.db.set_value(
            "Airplane Ticket",
            t,
            "gate_number",
            gate
        )


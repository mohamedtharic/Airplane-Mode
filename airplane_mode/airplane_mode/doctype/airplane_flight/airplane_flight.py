# Copyright (c) 2026, Tharic and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
class AirplaneFlight(WebsiteGenerator):
    
    def on_submit(self):
        self.status = "Completed"

    def on_update(self):
        frappe.enqueue(
            "airplane_mode.airplane_mode.utils.update_ticket_gates",
            flight=self.name,
            gate=self.gate_number
        )
    def update_ticket_gates(flight_name, gate_number):
        tickets = frappe.get_all(
            "Airplane Ticket",
            filters={"flight": flight_name},
            pluck="name"
            )
        for ticket in tickets:
            frappe.db.set_value(
                "Airplane Ticket",
                ticket,
                "gate_number",
                gate_number
                )
        frappe.db.commit()

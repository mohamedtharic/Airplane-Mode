# Copyright (c) 2026, Tharic and contributors
# For license information, please see license.txt

import frappe
import random
import string
from frappe.model.document import Document


class AirplaneTicket(Document):
    def validate(self):
        self.remove_duplicate_add_ons()
        self.calculate_total_amount()
    def calculate_total_amount(self):
        total = self.flight_price or 0
        for row in self.addons:
            total += row.amount or 0
        self.total_amount = total
    def remove_duplicate_add_ons(self):
        seen_items = set()
        unique_rows = []
        for row in self.addons:
            if row.item not in seen_items:
                seen_items.add(row.item)
                unique_rows.append(row)
        self.set("addons", unique_rows)
            
    def before_insert(self):
        self.set_random_seat()
        
    def set_random_seat(self):
        if self.seat:
            return
        
        number = random.randint(1, 99)   # random integer
        letter = random.choice(string.ascii_uppercase[:5])  # A–E
        self.seat = f"{number}{letter}"

class AirplaneTicket(Document):

    def validate(self):
        self.check_airplane_capacity()

    def check_airplane_capacity(self):

        if not self.flight:
            return

        # get flight document
        flight_doc = frappe.get_doc("Airplane Flight", self.flight)

        # get airplane from flight
        airplane = flight_doc.airplane

        # get airplane capacity
        capacity = frappe.db.get_value("Airplane", airplane, "capacity")

        # count tickets already booked for this flight
        ticket_count = frappe.db.count(
            "Airplane Ticket",
            {
                "flight": self.flight,
                "docstatus": ["!=", 2]   # ignore cancelled tickets
            }
        )

        # prevent overbooking
        if ticket_count >= capacity:
            frappe.throw("No seats available for this flight.")

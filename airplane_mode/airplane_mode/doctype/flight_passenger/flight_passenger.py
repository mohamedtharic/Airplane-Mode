# Copyright (c) 2026, Tharic and contributors
# For license information, please see license.txt

# import frappe
from typing import Self
from frappe.model.document import Document


class FlightPassenger(Document):
    def validate(self):
        first = self.first_name or ""
        last = self.last_name or ""
        self.full_name = f"{first} {last}".strip()

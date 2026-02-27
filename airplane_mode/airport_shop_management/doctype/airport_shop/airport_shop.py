# Copyright (c) 2026, Tharic and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document


class AirportShop(Document):
    def update_airport_shop_counts(airport):
        total = frappe.db.count("Airport Shop", {"airport": airport})
        occupied = frappe.db.count("Airport Shop", {
            "airport": airport,
            "status": "Occupied"
            })
        frappe.db.set_value("Airport", airport, {
            "total_shops": total,
            "occupied_shops": occupied,
            "available_shops": total - occupied
            })

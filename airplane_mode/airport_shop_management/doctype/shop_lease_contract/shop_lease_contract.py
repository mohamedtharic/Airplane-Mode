# Copyright (c) 2026, Tharic and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document
from datetime import timedelta

class ShopLeaseContract(Document):

    def on_submit(self):
        self.create_payment_schedule()

    def create_payment_schedule(self):

        current_date = self.start_date

        while current_date <= self.expiry_date:

            frappe.get_doc({
                "doctype": "Shop Rent Payment",
                "lease_contract": self.name,
                "due_date": current_date,
                "rent_amount": self.rent_amount,
                "status": "Unpaid"
            }).insert()

            # next month
            current_date = frappe.utils.add_months(current_date, 1)


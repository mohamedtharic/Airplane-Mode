import frappe

def get_context(context):

    context.shops = frappe.get_all(
        "Airport Shop",
        fields=["name", "shop_name", "area", "status"]
    )

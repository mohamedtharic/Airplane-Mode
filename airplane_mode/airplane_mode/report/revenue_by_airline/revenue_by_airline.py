import frappe
from frappe import _


def execute(filters=None):
    columns = get_columns()
    data = get_data()
    chart = get_chart(data)
    summary = get_summary(data)

    return columns, data, None, chart, summary


# -------------------------
# COLUMNS
# -------------------------
def get_columns():
    return [
        {
            "label": _("Airline"),
            "fieldname": "airline",
            "fieldtype": "Link",
            "options": "Airline",
            "width": 200,
        },
        {
            "label": _("Revenue"),
            "fieldname": "revenue",
            "fieldtype": "Currency",
            "width": 150,
        },
    ]


# -------------------------
# DATA
# -------------------------
def get_data():

    airlines = frappe.get_all("Airline", pluck="name")

    # get submitted tickets only
    tickets = frappe.get_all(
        "Airplane Ticket",
        filters={"docstatus": 1},
        fields=["flight", "flight_price"]
    )

    revenue_map = {a: 0 for a in airlines}

    for t in tickets:

        # get airplane from flight
        airplane = frappe.db.get_value(
            "Airplane Flight",
            t.flight,
            "airplane"
        )

        # get airline from airplane
        airline = frappe.db.get_value(
            "Airplane",
            airplane,
            "airline"
        )

        if airline:
            revenue_map[airline] += t.flight_price or 0

    data = []
    total = 0

    for airline in airlines:
        revenue = revenue_map.get(airline, 0)
        data.append({
            "airline": airline,
            "revenue": revenue
        })
        total += revenue


    return data


# -------------------------
# DONUT CHART
# -------------------------
def get_chart(data):

    labels = []
    values = []

    for row in data:
        if row["airline"] != "Total":
            labels.append(row["airline"])
            values.append(row["revenue"])

    return {
        "data": {
            "labels": labels,
            "datasets": [
                {
                    "name": "Revenue",
                    "values": values
                }
            ]
        },
        "type": "donut"
    }


# -------------------------
# SUMMARY
# -------------------------
def get_summary(data):

    total = sum(row["revenue"] for row in data if row["airline"] != "Total")

    return [
        {
            "value": total,
            "label": "Total Revenue",
            "datatype": "Currency",
        }
    ]


import frappe


def get_context(context):
    context.no_cache = 1
    context.title = "MYL Blood Connect"

    context.units = frappe.get_all(
        "Unit",
        fields=["name"],
        order_by="name asc",
    )


@frappe.whitelist(allow_guest=True)
def search_donors(unit=None, blood_group=None):
    filters = {}

    if unit:
        filters["unit"] = unit

    if blood_group:
        allowed_groups = [
            "A+", "A-", "B+", "B-",
            "O+", "O-", "AB+", "AB-",
        ]

        if blood_group not in allowed_groups:
            frappe.throw("Invalid blood group")

        filters["blood_group"] = blood_group

    return frappe.get_all(
        "Blood Donor",
        filters=filters,
        fields=[
            "full_name",
            "house_name",
            "unit",
            "blood_group",
            "mobile_number",
        ],
        order_by="full_name asc",
        limit_page_length=100,
    )

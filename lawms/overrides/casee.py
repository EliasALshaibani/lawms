from lawms.lawms.overrides.casee import umalqurra
from datetime import datetime
import frappe

@frappe.whitelist()
def convert_to_hijri(gregorian_date):
"""
Convert Gregorian date to Hijri using Umm al-Qura calendar
:param gregorian_date: Gregorian date (YYYY-MM-DD)
:return: Hijri date in the format YYYY-MM-DD
"""

    try:
        if not gregorian_date:
            frappe.throw("الرجاء إدخال تاريخ ميلادي صالح.")

        gregorian_date_obj = datetime.strptime(gregorian_date, "%Y-%m-%d")
        hijri_date = HijriDate(gregorian_date_obj.year, gregorian_date_obj.month, gregorian_date_obj.day, adjust=False)
        return f"{hijri_date.year}-{hijri_date.month:02d}-{hijri_date.day:02d}"
    except Exception as e:
        frappe.throw(f"حدث خطأ أثناء تحويل التاريخ: {str(e)}")

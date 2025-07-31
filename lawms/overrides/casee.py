from lawms.lawms.overrides.casee import umalqurra
from datetime import datetime
import frappe

@frappe.whitelist()
def convert_to_hijri(gregorian_date):
    """
    تحويل التاريخ الميلادي إلى هجري باستخدام مكتبة أم القرى
    :param gregorian_date: التاريخ الميلادي (YYYY-MM-DD)
    :return: التاريخ الهجري بصيغة YYYY-MM-DD
    """
    try:
        # التحقق من صحة الإدخال
        if not gregorian_date:
            frappe.throw("الرجاء إدخال تاريخ ميلادي صالح.")

        # تحويل النص إلى كائن datetime
        gregorian_date_obj = datetime.strptime(gregorian_date, "%Y-%m-%d")
        # استخدام مكتبة أم القرى للتحويل
        hijri_date = HijriDate(gregorian_date_obj.year, gregorian_date_obj.month, gregorian_date_obj.day, adjust=False)
        return f"{hijri_date.year}-{hijri_date.month:02d}-{hijri_date.day:02d}"
    except Exception as e:
        frappe.throw(f"حدث خطأ أثناء تحويل التاريخ: {str(e)}")

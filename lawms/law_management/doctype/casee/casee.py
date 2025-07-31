# Copyright (c) 2024, elias Alshaibani and contributors
# For license information, please see license.txt

# import frappe
#from frappe.model.document import Document

#class Casee(Document):
#	pass

import frappe
from hijri_converter import convert
from datetime import datetime
from frappe.model.document import Document

class Casee(Document):
    def validate(self):
        """
        تحويل التاريخ الميلادي إلى هجري مع تضمين اليوم عند حفظ المستند.
        """
        if self.gregorian_date:  # التأكد من وجود التاريخ الميلادي
            try:
                self.hijri_date = convert_to_hijri_with_day(self.gregorian_date)
            except Exception as e:
                frappe.throw(f"حدث خطأ أثناء تحويل التاريخ الميلادي إلى هجري: {str(e)}")

def convert_to_hijri_with_day(gregorian_date):
    try:
        # تحويل النص إلى كائن تاريخ ميلادي
        gregorian_date_obj = datetime.strptime(gregorian_date, "%Y-%m-%d")
        # تحويل التاريخ الميلادي إلى هجري
        hijri_date = convert.Gregorian(
            gregorian_date_obj.year,
            gregorian_date_obj.month,
            gregorian_date_obj.day
        ).to_hijri()
        # استخدام مكتبة datetime لإيجاد اسم اليوم
        day_name = get_day_name(gregorian_date_obj)
        # إرجاع التاريخ الهجري مع اليوم
        return f"{hijri_date.year}-{hijri_date.month:02d}-{hijri_date.day:02d} {day_name}"
    except ValueError:
        raise ValueError("تنسيق التاريخ الميلادي غير صحيح. الرجاء إدخال التاريخ بصيغة YYYY-MM-DD.")
    except Exception as e:
        raise Exception(f"خطأ غير متوقع أثناء التحويل: {str(e)}")

def get_day_name(date_obj):
    # استخدام مكتبة datetime لتحديد اسم اليوم
    days = ["الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة", "السبت", "الأحد"]
    return days[date_obj.weekday()]
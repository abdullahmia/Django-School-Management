from django.contrib import admin

from .models import AttendanceReport

class AttendanceReportAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'semester', 'department', 'subjects', 'class_date']
    list_per_page = 20

admin.site.register(AttendanceReport, AttendanceReportAdmin)
from django.urls import path
from . import views


app_name = 'attendance_reporting'

urlpatterns = [
    path('attendance-reporting/', views.attendance_reporting_index, name='attendance_reporting'),
    path('attendance-reporting-data/', views.attendance_reporting_class_record, name='attendance_reporting_data'),
    path('attendance-reporting-add-data/', views.attendance_reporting_add_form, name='attendance_reporting_add_data'),
    path('attendance-reporting-teacher-recent-entries/', views.attendance_reporting_teacher_recent_entries, name='attendance_reporting_teacher_recent_entries'),
]
from django import forms
from .models import AttendanceReport

class AddAttendanceReportForm(forms.ModelForm):
    class Meta:
        model = AttendanceReport
        fields = "__all__"
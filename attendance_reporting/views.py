from django.shortcuts import render, HttpResponse

from academics.models import Department, Subject, Semester

from .forms import AddAttendanceReportForm

# Create your views here.
def attendance_reporting_index(request):
    semesters = Semester.objects.all()
    for i in semesters:
        print(i)

    department = Department.objects.all()
    for x in department:
        print(x)

    subject = Subject.objects.all()
    for z in subject:
        print(z)


    return render(request, 'attendance_reporting/report_dashboard.html')


def attendance_reporting_class_record(request):
    return render(request, 'attendance_reporting/attendance_report_all_data.html')


def attendance_reporting_add_form(request):
    semesters = Semester.objects.all()
    form = AddAttendanceReportForm(request.POST)
    ctx = {
        'semesters': semesters,
        'form': form,

    }
    return render(request, 'attendance_reporting/attendance_report_form.html', ctx)


def attendance_reporting_teacher_recent_entries(request):
    return render(request, 'attendance_reporting/attendance_reporting_teacher_recent_entries.html')




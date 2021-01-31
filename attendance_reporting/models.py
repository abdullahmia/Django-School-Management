from django.db import models
from academics.models import Subject, Semester, Department
from teachers.models import Teacher

# Create your models here.
class AttendanceReport(models.Model):

    is_assignment_is_quiz = (
        ('yes', 'Yes'),
        ('no', 'No'),

    )

    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    class_date = models.DateField(max_length=255)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    subjects = models.ForeignKey(Subject, on_delete=models.CASCADE)
    place_class_taken = models.CharField(max_length=255)
    class_duration = models.CharField(max_length=255)
    attend_student = models.IntegerField(default=0)
    total_class_remain_student = models.IntegerField(default=0)
    average = models.CharField(max_length=10)
    is_assignment = models.CharField(max_length=5, choices=is_assignment_is_quiz, default=is_assignment_is_quiz[0][0])
    is_quiz = models.CharField(max_length=5, choices=is_assignment_is_quiz, default=is_assignment_is_quiz[0][0])
    phone_call_quantity = models.IntegerField(default=0)
    class_video_link = models.URLField()
    entry_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
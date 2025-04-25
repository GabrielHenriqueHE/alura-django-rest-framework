from django.db import models

from apps.escola.models.course_model import Course
from apps.escola.models.student_model import Student


class Registration(models.Model):
    PERIOD = (("M", "Morning"), ("A", "Afternoon"), ("N", "Nocturnal"))

    student = models.ForeignKey(Student, null=False, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)
    period = models.CharField(
        max_length=1, choices=PERIOD, blank=False, null=False, default="M"
    )

    def __str__(self):
        return f"{self.student.name} - {self.course.code} ({self.period})"

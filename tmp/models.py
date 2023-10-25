from django.db import models
from django.utils import timezone


class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    grade = models.CharField(max_length=4)
    year = models.PositiveIntegerField(default=2023)
    RollNo = models.CharField(max_length=30,default='Fa-')
    photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)


    def __str__(self):
        return self.name


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now().date())
    is_present = models.CharField(
        max_length=7,
        choices=[("Present", "Present"), ("Absent", "Absent")],
        default="Present"
    )

    def __str__(self):
        return f"{self.student.name} - {self.date}"

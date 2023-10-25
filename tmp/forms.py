from django import forms
from .models import Student, Attendance


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'course', 'grade', 'year','RollNo','photo']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'date', 'is_present']
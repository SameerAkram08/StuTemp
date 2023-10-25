from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from tmp.forms import StudentForm, AttendanceForm
from tmp.models import Student, Attendance


def my_view(request):
    return render(request, 'mytemplate.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST ,  request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})

def student_table(request):
    students = Student.objects.all()
    return render(request, 'student_table.html', {'students': students})

def generate_id_cards(request):
    students = Student.objects.all()
    return render(request, 'id_cards.html', {'students': students})

def record_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'attendance_form.html', {'form': form})



def attendance_list(request):
    # Retrieve all attendance records
    attendance_records = Attendance.objects.all()

    # You can filter and order records as needed, for example:
    # attendance_records = Attendance.objects.filter(date__year=2023).order_by('date')

    return render(request, 'attendance_list.html', {'attendance_records': attendance_records})

from django.shortcuts import render, redirect
from .models import Student

# Create your views here.

def add_student(request):
    if request.method == "POST":
        Student.objects.create(
            name = request.POST['name'],
            email = request.POST['email'],
            course = request.POST['course'],
            age = request.POST['age']
        )
        return redirect('student_list')
    return render(request, 'add_student.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students' : students})

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student_list')



from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home(request):
    return render(request, 'home.html')

def Attendance(request):
    return HttpResponse('Attendance Added')

def Admission(request):
    return HttpResponse('Admission Successful')


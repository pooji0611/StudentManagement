from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home),
    path('attendance/',views.Attendance),
    path('admission/',views.Admission),
]
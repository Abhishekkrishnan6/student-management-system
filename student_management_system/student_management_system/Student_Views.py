
from django.shortcuts import render, redirect


def HOME(request):
    return render(request,'Student/home.html')


def STUDENT_VIEW_ATTENDANCE(request):
    return render(request,'Student/view_attendance.html')
from django.shortcuts import  render, redirect
from django.contrib.auth.decorators import  login_required
from student_management.models import  Course,Session_Year

@login_required(login_url='/')
def HOME(request):
    return render(request,'Hod1/home.html')

@login_required(login_url='/')
def ADD_STUDENT(request):
    course = Course.objects.all()
    session_year = Session_Year.objects.all()

    context = {
        'course':course,
        'session_year':session_year,
    }

    return render(request , 'Hod1/add_student.html',context)
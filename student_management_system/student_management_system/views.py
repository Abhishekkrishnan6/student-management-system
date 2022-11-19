from django.shortcuts import render , redirect ,HttpResponse

from student_management.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate , logout,login
from django.contrib import messages

def BASE(request):
    return render(request,'base.html')


def LOGIN(request):
    return render(request,'login.html')


def doLogin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request,username=request.POST.get('email'),
                                         password =request.POST.get('password'),)
        if user != None:
            login(request ,user)
            user_type = user.user_type
            if user_type == '1':
                return HttpResponse('this is hod panel')
            elif user_type == '2':
                return HttpResponse('this is staff panel')
            elif user_type == '3':
                return HttpResponse('this is student panel')
            else:
                messages.error(request,'Email and password are invalid')
                return redirect('login')
        else:
            messages.error(request, 'Email and password are invalid')
            return  redirect('login')



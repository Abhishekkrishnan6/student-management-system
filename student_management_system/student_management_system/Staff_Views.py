from django.shortcuts import render, redirect

from student_management.models import Staff,Staff_Notification


def HOME(request):
    return render(request,'Staff/home.html')


def NOTIFICATIONS(request):
    staff = Staff.objects.filter(admin = request.user.id)
    # print(staff)
    for i in staff:
        print(i.id)
    return render(request,'Staff/notification.html')
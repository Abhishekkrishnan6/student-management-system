from django.shortcuts import render, redirect
from django.contrib.auth.decorators import  login_required

from student_management.models import Staff,Staff_Notification,Staff_leave,Staff_Feedback,Subject,Session_Year
from django.contrib import messages

@login_required(login_url='/')
def HOME(request):
    return render(request,'Staff/home.html')

@login_required(login_url='/')
def NOTIFICATIONS(request):
    staff = Staff.objects.filter(admin = request.user.id)
    # print(staff)
    for i in staff:
        staff_id = i.id
        notification = Staff_Notification.objects.filter(staff_id = staff_id)

        context = {
            'notification':notification,
        }
    return render(request,'Staff/notification.html',context)

@login_required(login_url='/')
def STAFF_NOTIFICATION_MARK_AS_DONE(request,status):

    notification = Staff_Notification.objects.get(id = status)

    notification.status = 1
    notification.save()



    return redirect('notifications')

@login_required(login_url='/')
def STAFF_APPLY_LEAVE(request):
    staff = Staff.objects.filter(admin = request.user.id)
    # print(staff)
    for i in staff:
        staff_id = i.id
        staff_leave_history = Staff_leave.objects.filter(staff_id = staff_id)
        context = {
            'staff_leave_history':staff_leave_history
        }
        return render(request,'Staff/apply_leave.html',context)

@login_required(login_url='/')
def STAFF_APPLY_LEAVE_SAVE(request):
    if request.method == 'POST':
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')
        staff = Staff.objects.get(admin = request.user.id)

        leave = Staff_leave(
            staff_id = staff,
            date = leave_date,
            message = leave_message,

        )
        leave.save()
        messages.success(request,'Leave Successfully Send')
        return redirect('staff_apply_leave')


def STAFF_FEEDBACK(request):



    staff_id = Staff.objects.get(admin = request.user.id)

    feedback_history = Staff_Feedback.objects.filter(staff_id=staff_id)

    context={
        'feedback_history':feedback_history
    }
    return render(request,'Staff/feedback.html',context)


def STAFF_FEEDBACK_SAVE(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')
        staff = Staff.objects.get(admin = request.user.id)
        feedback = Staff_Feedback(
            staff_id = staff,
            feedback = feedback,
            feedback_reply = "",
        )
        feedback.save()
        return redirect('staff_feedback')


def STAFF_TAKE_ATTENDANCE(request):


    staff_id = Staff.objects.get(admin = request.user.id)
    subject = Subject.objects.filter(staff = staff_id)
    session_year = Session_Year.objects.all()
    context = {
        'subject':subject,
        'session_year':session_year,

    }
    return render(request,'Staff/take_attendance.html',context)
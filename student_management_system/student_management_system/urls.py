
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from .import views,Hod_Views,Staff_Views,Student_Views
#
# from django.views.static import serve
# from django.conf.urls import url


urlpatterns = [
    path("admin/", admin.site.urls), #not working
    path("base/" , views.BASE,name='base'),
    #login path
    path("" ,views.LOGIN,name='login' ),
    path('doLogin',views.doLogin,name='doLogin'), #not working
    path('doLogout',views.doLogout,name='logout'),
    #prfolie update
    path('Profile',views.PROFILE,name='profile'),
    path('Profile/update',views.PROFILE_UPDATE,name='profile_update'),


    #this is hod pannel url


    path('Hod/Home',Hod_Views.HOME,name = 'hod_home'),
    path('Hod/Stuents/Add',Hod_Views.ADD_STUDENT,name = 'add_student'),
    path('Hod/Student/View',Hod_Views.VIEW_STUDENT,name = 'view_student'),
    path('Hod/Student/Edit/<str:id>',Hod_Views.EDIT_STUDENT,name = 'edit_student'),
    path('Hod/Student/Update',Hod_Views.UPDATE_STUDENT,name = 'update_student'),
    path('Hod/Student/Delete/<str:admin>',Hod_Views.DELETE_STUDENT,name = 'delete_student'),
    path('Hod/Staff/Leave_view',Hod_Views.STAFF_LEAVE_VIEW,name = 'staff_leave_view'),
    path('Hod/Staff/approve_leave/<str:id>',Hod_Views.STAFF_APPROVE_LEAVE,name = 'staff_approve_leave'),
    path('Hod/Staff/disapprove_leave/<str:id>',Hod_Views.STAFF_DISAPPROVE_LEAVE,name = 'staff_disapprove_leave'),

    #staff
    path('Hod/Staff/Add',Hod_Views.ADD_STAFF,name = 'add_staff'),
    path('Hod/Staff/View', Hod_Views.VIEW_STAFF, name='view_staff'),
    path('Hod/Staff/Edit/<str:id>', Hod_Views.EDIT_STAFF, name='edit_staff'),
    path('Hod/Staff/Update',Hod_Views.UPDATE_STAFF,name = 'update_staff'),
    #course

    path('Hod/Course/Add',Hod_Views.ADD_COURSE,name = 'add_course'),
    path('Hod/Course/View',Hod_Views.VIEW_COURSE,name = 'view_course'),
    path('Hod/Course/Edit/<str:id>',Hod_Views.EDIT_COURSE,name = 'edit_course'),
    path('Hod/Course/Update',Hod_Views.UPDATE_COURSE,name = 'update_course'),
    path('Hod/Course/Delete/<str:id>',Hod_Views.DELETE_COURSE,name = 'delete_course'),

    #subjects
    path('Hod/Subject/Add',Hod_Views.ADD_SUBJECT,name = 'add_subject'),
    path('Hod/Subject/View',Hod_Views.VIEW_SUBJECT,name = 'view_subject'),
    path('Hod/Subject/Edit/<str:id>',Hod_Views.EDIT_SUBJECT,name = 'edit_subject'),
    path('Hod/Subject/Update',Hod_Views.UPDATE_SUBJECT,name = 'update_subject'),
    path('Hod/Subject/Delete/<str:id>',Hod_Views.DELETE_SUBJECT,name = 'delete_subject'),

    #seasons
    path('Hod/Session/Add',Hod_Views.ADD_SESSION,name = 'add_session'),
    path('Hod/Session/View',Hod_Views.VIEW_SESSION,name = 'view_session'),
    path('Hod/Session/Edit/<str:id>',Hod_Views.EDIT_SESSION,name = 'edit_session'),
    path('Hod/Session/Update',Hod_Views.UPDATE_SESSION,name = 'update_session'),
    path('Hod/Session/Delete/<str:id>',Hod_Views.DELETE_SESSION,name = 'delete_session'),
    path('Hod/Staff/Send_Notification',Hod_Views.STAFF_SEND_NOTIFICATION,name = 'staff_send_notification'),
    path('Hod/Saff/save_notification',Hod_Views.SAVE_STAFF_NOTIFICATION,name = 'save_staff_notification'),
    path('Hod/Session/feedback',Hod_Views.STAFF_FEEDBACK,name = 'staff_feedback_reply'),
    path('Hod/Session/feedback_save',Hod_Views.STAFF_FEEDBACK_SAVE,name = 'staff_feedback_reply_save'),
    #this is staff url
    path('Staff/Home',Staff_Views.HOME,name = 'staff_home'),
    path('Staff/Notification',Staff_Views.NOTIFICATIONS,name = 'notifications'),
    path('Staff/mark_as_done/<str:status>',Staff_Views.STAFF_NOTIFICATION_MARK_AS_DONE,name = 'staff_notification_mark_as_done'),
    path('Staff/Apply_leave',Staff_Views.STAFF_APPLY_LEAVE,name = 'staff_apply_leave'),
    path('Staff/Apply_leave_save',Staff_Views.STAFF_APPLY_LEAVE_SAVE,name = 'staff_apply_leave_save'),
    path('Staff/Feedback',Staff_Views.STAFF_FEEDBACK,name = 'staff_feedback'),
    path('Staff/Feedback/Save', Staff_Views.STAFF_FEEDBACK_SAVE, name='staff_feedback_save'),
    path('Staff/Take_Attendance',Staff_Views.STAFF_TAKE_ATTENDANCE,name = 'staff_take_attendance'),

    path('Staff/save_Attendance', Staff_Views.STAFF_SAVE_ATTENDANCE, name='staff_save_attendance'),
    path('Staff/View_Attendance', Staff_Views.STAFF_VIEW_ATTENDANCE, name='staff_view_attendance'),

    #student url
    path('Student/Home', Student_Views.HOME, name='student_home'),
    path('Student/View_Attendance', Student_Views.STUDENT_VIEW_ATTENDANCE, name='student_view_attendance'),


#
#
# url(r'^media/(?p<path>.*)$', serve,{'document_root':        settings.MEDIA_ROOT}),
#
# url(r'^static/(?p<path>.*)$', serve,{'document_root':        settings.STATIC_ROOT}),

] + static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)

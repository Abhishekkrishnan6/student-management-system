
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from .import views,Hod_Views,Staff_Views,Student_Views





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
    #student url
    path('Student/Home', Student_Views.Home, name='student_home'),



] + static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)

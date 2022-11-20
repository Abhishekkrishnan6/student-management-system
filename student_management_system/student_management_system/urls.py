
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


    path('Hod/Home',Hod_Views.HOME,name = 'hod_home')


] + static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)

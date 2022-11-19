
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from .import views,Hod_Views,Staff_Views,Student_Views





urlpatterns = [
    path("admin/", admin.site.urls),
    path("base/" , views.BASE,name='base'),
    #login path
    path("" ,views.LOGIN,name='login' ),
    path('doLogin',views.doLogin,name='doLogin'),
    #this is hod pannel url

    path('HOD/Home',Hod_Views.HOME,name = 'home')


] + static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)

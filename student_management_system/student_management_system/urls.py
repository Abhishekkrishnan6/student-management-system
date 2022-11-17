
from django.contrib import admin
from django.urls import path
#import static
from django.conf import settings
from django.conf.urls.static import static
from .import views,Hod_Views,Staff_Views,Student_Views


urlpatterns = [
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL,docuament_root= settings.MEDIA_ROOT)

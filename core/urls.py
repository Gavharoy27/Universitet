from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view),
    path('yonalishlar/', yonalishlar_view, name = 'yonalishlar'),
    path('yonalishlar/<int:yonalish_id>/', yonalish_details_view),
    path('fanlar/', fanlar_view, name = 'fanlar'),
    path('fanlar/<int:fan_id>/', fan_details_view),
    path('ustozlar/', ustozlar_view, name = 'ustozlar'),
    path('ustozlar/<int:ustoz_id>/', ustoz_details_view),
    path('fan/<int:pk>/delete/', fan_d_view),
    path('yonalish/<int:pk>/delete/', yonalish_d_view),
    path('ustoz/<int:pk>/delete/', ustoz_d_view),
    path('fan/<int:pk>/update/', fan_update_view),
    path('yonalish/<int:pk>/update/', yonalish_update_view),
    path('ustoz/<int:pk>/update/', ustoz_update_view),
]





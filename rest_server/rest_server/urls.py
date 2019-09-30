from django.contrib import admin
from django.urls import path, include
from server import views


urlpatterns = [
    path('api/memory', views.view_mem),
    path('api/memory/<int:pk>', views.view_mem),
    path('api/cpu', views.view_cpu),
    path('api/cpu/<int:pk>', views.view_cpu),
    path('api/cpu/server_list', views.view_serverlist),
    path('api/cpu/<server_name>', views.view_serverlist),
    path('admin/', admin.site.urls),
]

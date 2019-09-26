from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from server import views


urlpatterns = [
    path('api/memory/', views.view_mem),
    path('api/cpu/', views.view_cpu),
    path('admin/', admin.site.urls),
]

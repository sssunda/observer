from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from server import views


urlpatterns = [
    path('', views.view),
    path('admin/', admin.site.urls),
]

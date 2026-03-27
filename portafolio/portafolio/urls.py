from django.contrib import admin
from django.urls import path
from dev2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hoja_vida, name='home'),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('dev2.urls')),   # TU APP
    path('admin/', admin.site.urls),
]
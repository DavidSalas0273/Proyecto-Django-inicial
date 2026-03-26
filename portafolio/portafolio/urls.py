from django.contrib import admin
from django.urls import path
from dev3 import views  # 👈 IMPORTANTE

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hoja_vida, name='home'),  # 👈 ESTA LÍNEA
]

from django.contrib import admin
from django.urls import path
from vehiculos import views as vehiculos_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vehiculos_views.lista_vehiculos, name='inicio'),
]

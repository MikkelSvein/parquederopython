from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vehiculos.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('tarifas/', include('tarifas.urls')),
    path('reservas/', include('reservas.urls')),
    path('dashboard/', include('dashboard.urls')),
]

from django.urls import path
from . import views
urlpatterns = [
    path('', views.lista_vehiculos, name='vehiculos_lista'),
    path('registrar/', views.registrar_vehiculo, name='registrar_vehiculo'),
    path('detalle/<int:pk>/', views.detalle_vehiculo, name='detalle_vehiculo'),
    path('eliminar/<int:pk>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
]

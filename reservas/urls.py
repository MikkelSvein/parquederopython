from django.urls import path
from . import views
urlpatterns = [
    path('', views.mis_reservas, name='mis_reservas'),
    path('crear/', views.crear_reserva, name='crear_reserva'),
]

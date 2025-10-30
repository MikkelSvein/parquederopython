from django.urls import path
from . import views
urlpatterns = [
    path('', views.ver_tarifas, name='ver_tarifas'),
    path('editar/', views.editar_tarifas, name='editar_tarifas'),
]

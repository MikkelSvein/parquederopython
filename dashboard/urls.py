from django.urls import path
from . import views
urlpatterns = [
    path('', views.panel, name='dashboard_panel'),
]

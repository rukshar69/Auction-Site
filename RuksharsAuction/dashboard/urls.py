from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
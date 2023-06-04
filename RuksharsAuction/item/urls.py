from django.urls import path

from . import views

app_name = 'item'

urlpatterns = [
    path('<int:pk>/', views.item_detail, name='detail'),
    path('place_bid/<int:pk>/', views.submit_bid, name='submit_bid'),
    path('new/', views.new_item, name='new_item'),
]
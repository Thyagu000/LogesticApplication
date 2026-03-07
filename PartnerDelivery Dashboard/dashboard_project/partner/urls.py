from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('orders/', views.orders, name='orders'),
    path('partners/', views.partners, name='partners'),
    path('payments/', views.payments, name='payments'),
    path('deliveries/', views.deliveries, name='deliveries'),
]
from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index'),
    path('client_orders/', views.client_orders, name='client_orders'),
]
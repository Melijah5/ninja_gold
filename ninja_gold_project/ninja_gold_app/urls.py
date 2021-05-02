from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add-money', views.add_money),
    path('reset' , views.reset),
]

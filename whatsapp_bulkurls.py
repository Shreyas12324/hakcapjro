# whatsapp_bulk/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send_messages/', views.send_messages, name='send_messages'),
   
]
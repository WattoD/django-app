from django.urls import path
from . import views

urlpatterns = [
    path('', views.messages, name='messages'),
    path('temp', views.temp_message, name='temp_message'),
]
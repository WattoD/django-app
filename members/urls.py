from django.urls import path
from . import views

urlpatterns = [
    path('', views.MessageListView.as_view(), name='messages'),
    path('delete/<int:id>/', views.MessageDeleteView.as_view(), name='message_delete'),
    path('temp', views.TemporaryMessageView.as_view(), name='temp_message'),
]
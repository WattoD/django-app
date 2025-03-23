from django.urls import path
from . import views

urlpatterns = [
    path('', views.TagsListView.as_view(), name='tags'),
]
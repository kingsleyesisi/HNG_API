from django.urls import path 
from . import views

urlpatterns = [
    path('info', views.GetInfo.as_view(), name='info')
]

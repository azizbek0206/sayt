
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Post, name='blog'),  # <-- MUHIM QISM: name='blog'
]

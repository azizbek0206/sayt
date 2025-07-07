# from django.urls import path
# from . import views

# urlpatterns = [
#     path('new/', views.order_create, name='order_create'),
#     path('thanks/', views.order_thanks, name='order_thanks'),
# ]

# orders/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Order, name='order'),  # <-- MUHIM: name='order'
]

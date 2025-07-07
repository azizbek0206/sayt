
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('contacts/', include('contact.urls')),
    path('menu/', include('menu.urls')),
    path('orders/', include('orders.urls')),
    path('testimonials/', include('testimonials.urls')),
    path('', include('home.urls')),
]


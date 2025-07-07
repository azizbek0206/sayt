from django.shortcuts import render
from .models import RestaurantInfo
# def index(request):
#     return HttpResponse("Bosh sahifaga xush kelibsiz!")

def list(request):
    items = RestaurantInfo.objects.all()
    return render(request, 'home/index.html', {'items': items})
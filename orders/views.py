from django.shortcuts import render, redirect
from .models import Order
from menu.models import MenuItem

def order_create(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        quantity = int(request.POST.get('quantity', 1))
        customer_name = request.POST.get('customer_name')
        item = MenuItem.objects.get(id=item_id)
        Order.objects.create(item=item, quantity=quantity, customer_name=customer_name)
        return redirect('order_thanks')
    items = MenuItem.objects.all()
    return render(request, 'orders/order_form.html', {'items': items})

def order_thanks(request):
    return render(request, 'orders/thanks.html')


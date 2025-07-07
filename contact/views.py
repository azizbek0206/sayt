from django.shortcuts import render, redirect
from .models import ContactMessage

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        ContactMessage.objects.create(name=name, email=email, message=message)
        return redirect('contact_thanks')
    return render(request, 'contacts/contact_form.html')

def contact_thanks(request):
    return render(request, 'contacts/thanks.html')


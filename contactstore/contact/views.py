from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import ContactForm
from .models import Contact 

# basic page
def home(request):  
    return render(request, 'contact/home.html')

# form page
def contactregister(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store')
    else:
        form = ContactForm()
    context = {'form':form}
    return render(request,'contact/contact-regist.html',context)

# show page
def store(request):
    contacts = Contact.objects.all()
    context = {'contacts':contacts}
    return render(request, 'contact/store.html',context)
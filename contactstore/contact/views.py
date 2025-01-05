from django.shortcuts import render, redirect
from django.http import HttpResponse  

def home(request):  
    return render(request, 'contact/home.html')

def contactregister(request):
    return render(request,'contact/contact-register.html')

def store(request):
    return render(request, 'contact/store.html')
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('register', views.contactregister, name='contact-regist'),
    path('store', views.store, name = 'store')
]


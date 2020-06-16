from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('index.html', views.Homepage, name = 'Homepage'),
    path('Bwahaha.html', views.Bwahaha, name = 'Bwahaha'),
    path('Contact.html', views.Contact, name = 'Contact'),
    path('AboutUs.html', views.AboutUs, name = 'About Us'),
]
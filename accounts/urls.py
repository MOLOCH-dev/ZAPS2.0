from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register, name = "register"),
    path("login", views.loginn, name = "login"),
    path("logout", views.logoutt, name = "logout"),
    path('', views.home, name = 'home'),
    path('index.html', views.Homepage, name = 'Homepage'),
    path('Bwahaha.html', views.Bwahaha, name = 'Bwahaha'),
    path('Contact.html', views.Contact, name = 'Contact'),
    path('AboutUs.html', views.AboutUs, name = 'About Us'),
]
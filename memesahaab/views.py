from django.shortcuts import render
from .models import Meme

# Create your views here.
def home(request):
    meme = Meme.objects.all

    return render(request, 'Homepage.html', {"meme": meme})

def Homepage(request):
    return render(request, 'index.html')

def Contact(request):
    return render(request, 'Contact.html')

def AboutUs(request):
    return render(request, 'AboutUs.html')

def Bwahaha(request):
    return render(request, 'Bwahaha.html')




        
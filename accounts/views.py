from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from memesahaab.views import Meme,Like

# Create your views here.

def loginn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('/')
    else:
        return render(request, 'login.html')



def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1!=password2:
            print("Passwords don't match")
            messages.info(request,'Passwords do not match')
            return redirect('register')

        elif User.objects.filter(username=username).exists():
            print("Username exists")
            messages.info(request,'Username Taken')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            print("Email exists")
            messages.info(request,'Email exists')
            return redirect('register')
        else:
            user = User.objects.create_user(username = username, password = password1, first_name =first_name, last_name = last_name, email = email)
            user.save()
            print("User created")
            messages.info(request,'User Created')
            return redirect('/')
    else:
        
        return render(request, "register.html")


def logoutt(request):
    auth.logout(request)
    return redirect('/')


def home(request):

    return render(request, 'Homepage.html')

def Homepage(request):
    memes = Meme.objects.all()
    user = request.user
    context = {
        'memes' : memes,
        'user' : user,
    }
    return render(request, 'index.html', context)

def Contact(request):
    return render(request, 'Contact.html')

def AboutUs(request):
    return render(request, 'AboutUs.html')

def Bwahaha(request):
    return render(request, 'Bwahaha.html')
from django.shortcuts import render, redirect
from .models import Meme,Like, Catg_Meme, Loss_Meme, Surreal_Meme, MemeMan_Meme, Like_Loss, Like_MemeMan
#from .views import Meme,Like, Catg_Meme
from .forms import MemeForm, LossForm, SurrealForm, MememanForm

# Create your views here.
def home(request):
#first displayed page

    return render(request, 'Home1.html')

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

def Catg(request):
    return render(request, 'Catg.html')

def Loss1(request):
    return render(request, 'Loss1.html')

def Surreal1(request):
    return render(request, 'Surreal1.html')

def MemeMan1(request):
    return render(request, 'MemeMan1.html')

def AboutUs(request):
    return render(request, 'AboutUs.html')

def Bwahaha(request):
    return render(request, 'Bwahaha.html')

def like_post(request):
    user = request.user
    if request.method == "POST":
        meme_id = request.POST.get('meme_id')
        meme_obj = Meme.objects.get(id = meme_id)
        if user in meme_obj.liked.all():
            meme_obj.liked.remove(user)
        else:
            meme_obj.liked.add(user)
        
        like, created = Like.objects.get_or_create(user=user, meme_id = meme_id)
        if not created:
            if like.value == "Like":

                like.value = "Unlike"
            else:
                like.value = "Like"
        like.save()
    return redirect('/')

def like_post_loss(request):
    user = request.user
    if request.method == "POST":
        meme_id = request.POST.get('meme_id')
        meme_obj = Loss_Meme.objects.get(id = meme_id)
        if user in meme_obj.liked.all():
            meme_obj.liked.remove(user)
        else:
            meme_obj.liked.add(user)
        
        like, created = Like_Loss.objects.get_or_create(user=user, meme_id = meme_id)
        if not created:
            if like.value == "Like":

                like.value = "Unlike"
            else:
                like.value = "Like"
        like.save()
    return redirect('loss_meme_listt')

def like_post_mememan(request):
    user = request.user
    if request.method == "POST":
        meme_id = request.POST.get('meme_id')
        meme_obj = MemeMan_Meme.objects.get(id = meme_id)
        if user in meme_obj.liked.all():
            meme_obj.liked.remove(user)
        else:
            meme_obj.liked.add(user)
        
        like, created = Like_MemeMan.objects.get_or_create(user=user, meme_id = meme_id)
        if not created:
            if like.value == "Like":

                like.value = "Unlike"
            else:
                like.value = "Like"
        like.save()
    return redirect('mememan_meme_listt')

#def post(request):
    
    #if request.method == 'POST':
       # catg_meme = request.POST['catg-meme']
       # catg_caption = request.POST['catg-caption']
       # catg_source = request.POST['catg-source']
    #else:
      #   return render(request, "Catg.html")

def Home1(request):
    return render(request, 'Home1.html')

def meme_list(request):
    Cgloss_memes = Loss_Meme.objects.all()
    return render(request, "Loss1.html", {'Cgloss_memes': Cgloss_memes})

def loss_meme_list(request):
    Cgloss_memes = Loss_Meme.objects.all()
    user = request.user
    return render(request, "Loss1.html", {'Cgloss_memes': Cgloss_memes, 'user':user})

def surreal_meme_list(request):
    Cgsurreal_memes = Surreal_Meme.objects.all()
    user = request.user
    return render(request, "Surreal1.html", {'Cgsurreal_memes': Cgsurreal_memes,'user':user})

def mememan_meme_list(request):
    Cgmememan_memes = MemeMan_Meme.objects.all()
    user = request.user
    return render(request, "MemeMan1.html", {'Cgmememan_memes': Cgmememan_memes, 'user':user})

def upload_meme(request):
    form = MemeForm()
    form1 = LossForm()
    form2 = MememanForm()
    form3 = SurrealForm()
    if request.method == 'POST':

        form1 = LossForm(request.POST, request.FILES)
        form2 = MememanForm(request.POST, request.FILES)
        form3 = SurrealForm(request.POST, request.FILES)
        if form1.is_valid():
            form1.save()
            print("saved")
            return redirect('/loss_meme_listt')
        else:
            form1 = LossForm()
        if form2.is_valid():
            form2.save()
            print("saved")
            return redirect('/mememan_meme_listt')
        else:
            form2 = MememanForm()

        if form3.is_valid():
            form3.save()
            print("saved")
            return redirect('/surreal_meme_listt')
        else:
            form3 = SurrealForm()
    return render(request, "uploaded.html", {'form': form, 'form1': form1, 'form2': form2, 'form3': form3})

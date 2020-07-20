from django.urls import path
from . import views
from .views import Homepage, Bwahaha, Contact, meme_list, upload_meme,loss_meme_list, Home1, home, Surreal1, MemeMan1, like_post_loss, like_post_mememan
app_name = 'memesahaab'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('Home1', views.Home1, name = 'Home1'),
    path('Bwahaha.html', views.Bwahaha, name = 'Bwahaha'),
    path('Contact.html', views.Contact, name = 'Contact'),
    path('AboutUs.html', views.AboutUs, name = 'AboutUs'),
    path('like/', views.like_post, name = 'like_post'),
    path('like_loss/', views.like_post_loss, name = 'like_post_loss'),
    path('like_mememan/', views.like_post_mememan, name = 'like_post_mememan'),
    path('Catg.html', views.Catg, name = 'Catg'),
    path('Loss1.html', views.Loss1, name = 'Loss1'),
    path('Surreal1.html', views.Surreal1, name = 'Surreal1'),
    path('MemeMan1.html', views.MemeMan1, name = 'MemeMan1'),
    path('Loss1.html', views.Loss1, name = 'Loss1'),
    path('meme_listt', views.meme_list, name = 'meme_listt'),
    path('loss_meme_listt', views.meme_list, name = 'loss_meme_listt'),
    path('surreal_meme_listt', views.surreal_meme_list, name = 'surreal_meme_listt'),
    path('mememan_meme_listt', views.mememan_meme_list, name = 'mememan_meme_listt'),
    path('uploaded.html', views.upload_meme, name = 'upload_meme'),
 
]
#   path('post/', views.post, name = "catg-post")
    #path('memes/upload', views.upload_meme, name = 'upload_meme'),

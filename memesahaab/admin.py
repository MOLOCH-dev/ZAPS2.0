from django.contrib import admin
from .models import Meme, Like, Category

admin.site.register(Meme)
admin.site.register(Like)
admin.site.register(Category)

# Register your models here.

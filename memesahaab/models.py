from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meme(models.Model):
    title = models.CharField(max_length = 100)
    img = models.ImageField(upload_to = "pics")
    desc = models.TextField()
    liked = models.ManyToManyField(User, default = None, blank = True, related_name= "liked")
    updated = models.DateTimeField(auto_now = True)
    created =models.DateTimeField(auto_now_add= True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name= "author")
    trending = models.BooleanField(default = False)
    def __str__(self):
        return str(self.title)

    @property
    def num_likes(self):
        return self.liked.all().count()

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
    )




class Category(models.Model):
    meme_name = models.ForeignKey(Meme, on_delete= models.CASCADE)
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return str(self.category_name)
    #if Category.objects.filter(category_name = category_name).exists():
    # messages.info(request,'Username Taken')   

    class Meta:
        ordering = ['category_name']

class Catg_Meme(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    caption = models.TextField()
    catg_meme = models.ImageField(upload_to = 'uploaded.html', null = True, blank = True)
    meme_file = models.FileField(upload_to = 'uploaded.html')

    def __str__(self):
        return self.title

class Loss_Meme(models.Model):
    title = models.CharField(max_length = 100, null=True, blank=True)
    author = models.CharField(max_length = 100,null=True, blank=True)
    caption = models.TextField(null=True, blank=True)
    loss_meme = models.ImageField(upload_to = 'uploaded.html', null = True, blank = True)
    loss_meme_comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class Surreal_Meme(models.Model):
    title = models.CharField(max_length = 100,null=True, blank=True)
    author = models.CharField(max_length = 100,null=True, blank=True)
    caption = models.TextField(null=True, blank=True)
    surreal_meme = models.ImageField(upload_to = 'uploaded.html', null = True, blank = True)
    surreal_meme_comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class MemeMan_Meme(models.Model):
    title = models.CharField(max_length = 100,null=True, blank=True)
    author = models.CharField(max_length = 100,null=True, blank=True)
    caption = models.TextField(null=True, blank=True)
    mememan_meme = models.ImageField(upload_to = 'uploaded.html', null = True, blank = True)
    mememan_meme_comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Like(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meme = models.ForeignKey(Meme, on_delete= models.CASCADE)
            
    value = models.CharField(max_length = 10, choices = LIKE_CHOICES, default = 'Like')

    def __str__(self):
        return str(self.meme)

class Like_Loss(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meme = models.ForeignKey(Loss_Meme, on_delete= models.CASCADE)
            
    value = models.CharField(max_length = 10, choices = LIKE_CHOICES, default = 'Like')

    def __str__(self):
        return str(self.meme)



class Like_MemeMan(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meme = models.ForeignKey(MemeMan_Meme, on_delete= models.CASCADE)
            
    value = models.CharField(max_length = 10, choices = LIKE_CHOICES, default = 'Like')

    def __str__(self):
        return str(self.meme)
#class Categories(models.Model):
 #   categories = models.ForeignKey(Category, on_delete = models.CASCADE)
  #  CATEGORY = "CG"
 #   CATEGORY_CHOICES = []
  #  for id in range(len(categories_list)):
   #     CATEGORY_CHOICES.append((CATEGORY+str(id), str(categories_list[id])))
    #Categories_list = models.CharField(max_length = 100, choices = CATEGORY_CHOICES, default = None)

    #def __str__(self):
     #   return str(self.Categories.list)

      #  class Meta:
       #     ordering = ['categories'] 
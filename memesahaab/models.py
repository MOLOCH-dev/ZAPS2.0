from django.db import models

# Create your models here.
class Meme(models.Model):
    name = models.CharField(max_length = 100)
    img = models.ImageField(upload_to = "pics")
    desc = models.TextField()
    likes = models.IntegerField()
    trending = models.BooleanField(default = False)
    
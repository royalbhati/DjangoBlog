from django.db import models
from django.contrib.auth.models import User
from blog.models import Post
# Create your models here.
class Profile(models.Model):
     user=models.OneToOneField(User,on_delete=models.CASCADE)
     dp=models.ImageField(default="default.jpg",upload_to="profile_pics")
     saved=models.ManyToManyField(Post,related_name="saved",blank=True)
     def __str__(self):
         return f'{self.user.username} Profile'
     
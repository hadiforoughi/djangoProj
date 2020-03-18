from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class protfoluser (models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    prourl= models.URLField(blank=True)
    profilepic=models.ImageField(blank=True,upload_to='pictures/userprofile')

    def __str__(self):
        return self.user.first_name
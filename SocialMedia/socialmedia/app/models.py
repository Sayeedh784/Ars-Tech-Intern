from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class AddDay(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  text = models.TextField(null=True,blank=True)
  album = models.ImageField(upload_to='images/',null=True,blank=True)
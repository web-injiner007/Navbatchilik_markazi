from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

from config import settings


# Create your models here.
class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    h_qism = models.CharField(max_length=100,blank=True,null=True)
    lavozim = models.CharField(max_length=100,blank=True,null=True)
    date_brith = models.DateTimeField(blank=True, null=True)
    photo = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    phone = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.user.username



class Tadbir(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    h_qism = models.CharField(max_length=100)
    aloqa_t = models.CharField(max_length=100)
    fayl = models.FileField(upload_to='tadbir_hujjatlari', blank=True, null=True)
    asosiy_q = RichTextField()


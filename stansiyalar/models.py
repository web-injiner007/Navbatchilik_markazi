from django.core.validators import RegexValidator
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class BazaStansiya(models.Model):
    nomeri = models.CharField(max_length=100)
    ip_manzili = models.GenericIPAddressField(protocol='IPv4')
    is_active = models.BooleanField(default=False)
    jolashuvi = models.CharField(max_length=60)
    koorX = models.FloatField(blank=True, null=True)
    koorY = models.FloatField(blank=True, null=True)
    model = models.CharField(max_length=100)
    yil = models.DateField(blank=True, null=True)
    toliq_mal = RichTextField()
    javob_shax = models.TextField(blank=True, null=True)
    ichki_nom = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nomeri

class ATS(models.Model):
    nomeri = models.CharField(max_length=100)
    ip_manzili = models.GenericIPAddressField(protocol='IPv4')
    is_active = models.BooleanField(default=False)
    jolashuvi = models.CharField(max_length=60)
    koorX = models.FloatField(blank=True, null=True)
    koorY = models.FloatField(blank=True, null=True)
    model = models.CharField(max_length=100)
    yil = models.DateField(blank=True, null=True)
    toliq_mal = RichTextField()
    javob_shax = models.TextField(blank=True, null=True)
    ichki_nom = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nomeri

class Hudud(models.Model):
    nomi = models.CharField(max_length=100)
    holat = models.BooleanField(default=False)

    def __str__(self):
        return self.nomi

class Ipmanzil(models.Model):

    kategoriya = (
        ('BazaStansiya', 'BazaStansiya'),
        ('ATS', 'ATS'),
        ('Kompyuter', 'Kompyuter'),
        ('Telefon', 'Telefon'),
        ('Server', 'Server'),
        ('Printer', 'Printer'),
        ('Router', 'Router'),
        ('PanasonicATS', 'PanasonicATS'),
        ('GrandstreamATS', 'GrandstreamATS'),
    )

    nomeri = models.CharField(max_length=100)
    kategoriya = models.CharField(max_length=100, choices=kategoriya)
    ip_manzili = models.GenericIPAddressField(protocol='IPv4',unique=True)
    is_active = models.BooleanField(default=False)
    last_checked = models.DateTimeField(auto_now=True)
    hudud = models.ForeignKey(Hudud, on_delete=models.CASCADE)
    koorX = models.FloatField(blank=True, null=True)
    jolashuvi = models.CharField(max_length=60)
    koorX = models.FloatField(blank=True, null=True)
    koorY = models.FloatField(blank=True, null=True)
    model = models.CharField(max_length=100)
    yil = models.DateField(blank=True, null=True)
    toliq_mal = RichTextField()
    javob_shax = RichTextField()
    ichki_nomer = RichTextField()

    def __str__(self):
        return self.nomeri








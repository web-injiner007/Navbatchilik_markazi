from django.core.validators import RegexValidator
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class GATS(models.Model):
    turi = (
        ('GrandStreamATS', 'GrandStreamATS'),
        ('Server', 'Server'),
        ('Printer', 'Printer'),
        ('Boshqa', 'Boshqa'),)

    hudud = (('Toshkent', 'Toshkent'),
             ('Toshkent_shahar', 'Toshkent_shahar'),
             ('Andijon', 'Andijon'),
             ('Namangan', 'Namangan'),
             ('Fargona', 'Fargona'),
             ('Sirdaryo', 'Sirdaryo'),
             ('Jizzax', 'Jizzax'),
             ('Samarqand', 'Samarqand'),
             ('Qashqadaryo', 'Qashqadaryo'),
             ('Buxoro', 'Buxoro'),
             ('Surxondaryo', 'Surxondaryo'),
             ('Navoiy', 'Navoiy'),
             ('Xorazim', 'Xorazim'),
             ('Qoraqalpogiston', 'Qoraqalpogiston'),
             )
    nomeri = models.CharField(max_length=100)
    turi = models.CharField(max_length=100, choices=turi)
    ip_manzili = models.GenericIPAddressField(protocol='IPv4')
    is_active = models.BooleanField(default=False)
    last_checked = models.DateTimeField(auto_now=True)
    hudud = models.TextField(max_length=40, choices=hudud)
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

class PATS(models.Model):
    toifa = (
        ('PanasonicATS', 'PanasonicATS'),
        ('Server', 'Server'),
        ('Printer', 'Printer'),
        ('Boshqa', 'Boshqa'),)

    hudud = (('Toshkent', 'Toshkent'),
             ('Toshkent_shahar', 'Toshkent_shahar'),
             ('Andijon', 'Andijon'),
             ('Namangan', 'Namangan'),
             ('Fargona', 'Fargona'),
             ('Sirdaryo', 'Sirdaryo'),
             ('Jizzax', 'Jizzax'),
             ('Samarqand', 'Samarqand'),
             ('Qashqadaryo', 'Qashqadaryo'),
             ('Buxoro', 'Buxoro'),
             ('Surxondaryo', 'Surxondaryo'),
             ('Navoiy', 'Navoiy'),
             ('Xorazim', 'Xorazim'),
             ('Qoraqalpogiston', 'Qoraqalpogiston'),
             )

    nomeri = models.CharField(max_length=100)
    toifa = models.CharField(max_length=100, choices=toifa)
    ip_manzili = models.GenericIPAddressField(protocol='IPv4')
    is_active = models.BooleanField(default=False)
    last_checked = models.DateTimeField(auto_now=True)
    hudud = models.TextField(max_length=40, choices=hudud)
    koorX = models.FloatField(blank=True, null=True)
    jolashuvi = models.CharField(max_length=60)
    koorY = models.FloatField(blank=True, null=True)
    model = models.CharField(max_length=100)
    yil = models.DateField(blank=True, null=True)
    toliq_mal = RichTextField()
    javob_shax = RichTextField()
    ichki_nomer = RichTextField()
    def __str__(self):
        return self.nomeri


from django.db import models
from ckeditor.fields import RichTextField


class Ipmanzil(models.Model):
    KATEGORIYA_CHOICES = (
        ('BazaStansiya', 'BazaStansiya'),
        ('PanasonicATS', 'PanasonicATS'),
        ('GrandStreamATS', 'GrandStreamATS'),
        ('Kompyuter', 'Kompyuter'),
        ('Telefon', 'Telefon'),
        ('Server', 'Server'),
        ('Printer', 'Printer'),
        ('Router', 'Router'),
        ('Boshqa', 'Boshqa'),
    )

    HUDUD_CHOICES = (
        ('Toshkent', 'Toshkent'),
        ('Andijon', 'Andijon'),
        ('Namangan', 'Namangan'),
        ('Fargona', 'Fargona'),
        ('Sirdaryo', 'Sirdaryo'),
        ('Jizzax', 'Jizzax'),
        ('Samarqand', 'Samarqand'),
        ('Qashqadaryo', 'Qashqadaryo'),
        ('Buxoro', 'Buxoro'),
        ('Surxondaryo', 'Surxondaryo'),
        ('Navoiy', 'Navoiy'),
        ('Toshkent_shahar', 'Toshkent_shahar'),
        ('Xorazim', 'Xorazim'),
        ('Qoraqalpogiston', 'Qoraqalpogiston'),
    )

    nomeri = models.CharField(max_length=100)
    kategoriya = models.CharField(max_length=100, choices=KATEGORIYA_CHOICES)
    ip_manzili = models.GenericIPAddressField(protocol='IPv4')
    is_active = models.BooleanField(default=False)
    last_checked = models.DateTimeField(auto_now=True)
    hudud = models.CharField(max_length=40, choices=HUDUD_CHOICES)  # Hudud uchun CharField
    koorX = models.FloatField(blank=True, null=True)
    koorY = models.FloatField(blank=True, null=True)
    jolashuvi = models.CharField(max_length=60)
    model = models.CharField(max_length=100)
    yil = models.DateField(blank=True, null=True)
    toliq_mal = RichTextField()
    javob_shax = RichTextField()
    ichki_nomer = RichTextField()

    def __str__(self):
        return self.nomeri








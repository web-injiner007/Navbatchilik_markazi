from django.contrib import admin
from .models import BazaStansiya,ATS,Ipmanzil,Hudud
# Register your models here.
@admin.register(BazaStansiya)
class BazaStansiyaAdmin(admin.ModelAdmin):
    list_display = ('nomeri','model','yil','toliq_mal')


@admin.register(ATS)
class ATSAdmin(admin.ModelAdmin):
    list_display = ('nomeri','model','yil','toliq_mal')

@admin.register(Ipmanzil)
class IpmanzilAdmin(admin.ModelAdmin):
    list_display = ('nomeri','ip_manzili','kategoriya','is_active','hudud','toliq_mal')

@admin.register(Hudud)
class HududAdmin(admin.ModelAdmin):
    list_display = ('nomi','holat')
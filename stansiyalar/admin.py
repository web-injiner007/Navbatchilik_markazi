from django.contrib import admin
from .models import GATS,PATS,Ipmanzil
# Register your models here.




@admin.register(GATS)
class GATSAdmin(admin.ModelAdmin):
    list_display =  ('nomeri','ip_manzili','turi','is_active','hudud','toliq_mal')


@admin.register(PATS)
class PATSAdmin(admin.ModelAdmin):
    list_display =  ('nomeri','ip_manzili','toifa','is_active','hudud','toliq_mal')

@admin.register(Ipmanzil)
class IpmanzilAdmin(admin.ModelAdmin):
    list_display = ('nomeri','ip_manzili','kategoriya','is_active','hudud','toliq_mal')
    search_fields = ['nomeri','ip_manzili','kategoriya','is_active','hudud','toliq_mal']


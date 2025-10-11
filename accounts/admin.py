from django.contrib import admin
from .models import Profil, ChatMessage,Tadbir


# Register your models here.

@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'lavozim', 'phone','h_qism','photo')

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'timestamp', 'message')


@admin.register(Tadbir)
class TadbirAdmin(admin.ModelAdmin):
    list_display = ['user','h_qism', 'aloqa_t', 'nomi', 'fayl', 'asosiy_q']

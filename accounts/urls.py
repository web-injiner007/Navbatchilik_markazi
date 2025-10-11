from .views import user_login, tadbir, phone, chat_view, send_message
from django.urls import path,include

urlpatterns = [
    path('',user_login,name='login'),
    path('tadbirlar/',tadbir,name='tadbir'),
    path('telefonlar/',phone,name='phone'),
    path('dashboard/',chat_view,name='dashboard'),
    path('dashboard/chats/send/', send_message, name='send_message'),
]

from .views import user_login, tadbir, phone,dashboard
from django.urls import path,include

urlpatterns = [
    path('',user_login,name='login'),
    path('tadbirlar/',tadbir,name='tadbir'),
    path('telefonlar/',phone,name='phone'),
    path('dashboard/',dashboard,name='dashboard'),
]

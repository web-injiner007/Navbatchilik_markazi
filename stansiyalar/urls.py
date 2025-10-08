from .views import index,ip_list_view
from django.urls import path,include

urlpatterns = [
    path('',index,name='index'),

    path('test/',ip_list_view,name='test'),
]

# from collections import defaultdict
# from accounts.models import Profil
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render
# from .tasks import update_ip_statuses
# from django.contrib import messages
# from .models import Ipmanzil,GATS
# # Create your views here.
#
# @login_required
# def index(request):
#     if request.user.is_authenticated:
#         user = request.user  #login qilgan foydalanuvchi
#         profile = Profil.objects.get(user=user)  # Foydalanuvchining profili
#     update_ip_statuses()
#     # update_gats_status1()
#
#     iplar = Ipmanzil.objects.filter(kategoriya="BazaStansiya").order_by('hudud')
#     iplar1 = Ipmanzil.objects.filter(kategoriya="GrandStreamATS").order_by('hudud')
#     iplar2 = Ipmanzil.objects.filter(kategoriya="PanasonicATS").order_by('hudud')
#     # hududlar = sorted(set((ip.hudud,ip.is_active) for ip in iplar))
#     #
#
#     # hududlar1 = sorted(set((ip1.hudud, ip1.is_active) for ip1 in iplar1))
#     #
#     # iplar2 = Ipmanzil.objects.all().order_by('hudud').filter(kategoriya="PanasonicATS")
#     # hududlar2 = sorted(set((ip2.hudud, ip2.is_active) for ip2 in iplar2))
#     # print(hududlar2)
#     # hududlar_status = defaultdict(lambda: True)
#     # for hudud in hududlar:
#     #     if iplar.filter(hudud=hudud, is_active=False).exists():
#     #         hududlar_status[hudud] = False
#     #         break
#     # for hudud in hududlar1:
#     #     if iplar1.filter(hudud=hudud, is_active=False).exists():
#     #         hududlar_status[hudud] = False
#     #         break
#     # for hudud in hududlar2:
#     #     if iplar2.filter(hudud=hudud, is_active=False).exists():
#     #         hududlar_status[hudud] = False
#     #         break
#     # iplar = Ipmanzil.objects.all()
#
#     hududlar = []
#     for h in set(ip.hudud for ip in iplar):
#         # Agar shu hududda is_active=False bo'lgan bitta ham IP bo'lsa
#         if Ipmanzil.objects.filter(hudud=h, is_active=False).exists():
#             holat = False
#         else:
#             holat = True
#         hududlar.append((h, holat))
#     hududlar1 = []
#     for h in set(ip1.hudud for ip1 in iplar1):
#         holat = not Ipmanzil.objects.filter(hudud=h, is_active=False).exists()
#         hududlar1.append((h, holat))
#
#     hududlar2 = []
#     for h in set(ip2.hudud for ip2 in iplar2):
#         holat = not Ipmanzil.objects.filter(hudud=h, is_active=False).exists()
#         hududlar2.append((h, holat))
#
#     # hududlar_status = defaultdict(lambda: True)
#     # for hudud in zonalar:
#     #     if manzillar.filter(hudud=hudud, is_active=False).exists():
#     #         hududlar_status[hudud] = False
#
#     context = {
#         'iplar': iplar,
#         'hududlar': hududlar,
#
#         'iplar1': iplar1,
#         'hududlar1': hududlar1,
#
#         'iplar2': iplar2,
#         'hududlar2': hududlar2,
#
#         'username': user.username,
#         'profile': profile.photo.url if profile.photo else None,
#     }
#     return render(request, 'index.html',  context)
#
#
# # from django.shortcuts import render
# # from .models import Ipmanzil
# # from .tasks import update_ip_statuses
# #
# # def ip_list_view(request):
# #     # update_ip_statuses()  # Har safar sahifa yuklanganda ping qiladi
# #     # ip_list = Ipmanzil.objects.all()
# #
# #     iplar = Ipmanzil.objects.all().order_by('hudud')
# #     hududlar = sorted(set(ip.hudud.nomi for ip in iplar))
# #
# #     return render(request, 'chat.html', {'iplar': iplar, 'hududlar': hududlar})
#
#
#
from collections import defaultdict
from accounts.models import Profil
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from .tasks import update_ip_statuses
from .models import Ipmanzil


@login_required
def index(request):
    user = request.user
    profile = Profil.objects.get(user=user)

    # IP holatlarini yangilash
    update_ip_statuses()

    # Har bir kategoriya uchun IPlar
    iplar = Ipmanzil.objects.filter(kategoriya="BazaStansiya").order_by('hudud')
    iplar1 = Ipmanzil.objects.filter(kategoriya="GrandStreamATS").order_by('hudud')
    iplar2 = Ipmanzil.objects.filter(kategoriya="PanasonicATS").order_by('hudud')

    # Har biri uchun yagona hududlar ro‘yxati va holati
    hududlar = []
    for h in sorted(set(ip.hudud for ip in iplar)):
        holat = not iplar.filter(hudud=h, is_active=False).exists()
        hududlar.append((h, holat))

    hududlar1 = []
    for h in sorted(set(ip.hudud for ip in iplar1)):
        holat = not iplar1.filter(hudud=h, is_active=False).exists()
        hududlar1.append((h, holat))

    hududlar2 = []
    for h in sorted(set(ip.hudud for ip in iplar2)):
        holat = not iplar2.filter(hudud=h, is_active=False).exists()
        hududlar2.append((h, holat))

    context = {
        'iplar': iplar,
        'hududlar': hududlar,

        'iplar1': iplar1,
        'hududlar1': hududlar1,

        'iplar2': iplar2,
        'hududlar2': hududlar2,

        'username': user.username,
        'profile': profile.photo.url if profile.photo else None,
    }

    return render(request, 'index.html', context)

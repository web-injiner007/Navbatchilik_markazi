from collections import defaultdict

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from .models import Ipmanzil,Hudud

# Create your views here.

@login_required
def index(request):
    update_ip_statuses()

    iplar = Ipmanzil.objects.all().order_by('hudud').filter(kategoriya="BazaStansiya")
    hududlar = sorted(set((ip.hudud.nomi,ip.hudud.holat) for ip in iplar))

    iplar1 = Ipmanzil.objects.all().order_by('hudud').filter(kategoriya="GrandstreamATS")
    hududlar1 = sorted(set((ip1.hudud.nomi, ip1.hudud.holat) for ip1 in iplar1))

    iplar2 = Ipmanzil.objects.all().order_by('hudud').filter(kategoriya="PanasonicATS")
    hududlar2 = sorted(set((ip2.hudud.nomi, ip2.hudud.holat) for ip2 in iplar2))



    context = {
        'iplar': iplar,
        'hududlar': hududlar,
        'iplar1': iplar1,
        'hududlar1': hududlar1,
        'iplar2': iplar2,
        'hududlar2': hududlar2,
    }
    return render(request, 'index.html',  context)



from django.shortcuts import render
from .models import Ipmanzil
from .tasks import update_ip_statuses

def ip_list_view(request):
    # update_ip_statuses()  # Har safar sahifa yuklanganda ping qiladi
    # ip_list = Ipmanzil.objects.all()

    iplar = Ipmanzil.objects.all().order_by('hudud')
    hududlar = sorted(set(ip.hudud.nomi for ip in iplar))

    return render(request, 'test.html', {'iplar': iplar, 'hududlar': hududlar})




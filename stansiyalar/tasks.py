import asyncio
import subprocess
from .models import Ipmanzil,GATS



def ping_ip_sync(ip):
    try:
        output = subprocess.run(["ping", "-n", "1", ip], capture_output=True, text=True)
        return ip, "TTL=" in output.stdout

    except Exception:
        return ip, False

async def ping_ip(ip, loop):
    return await loop.run_in_executor(None, ping_ip_sync, ip)




async def ping_all(ips):
    loop = asyncio.get_event_loop()
    tasks = [ping_ip(ip, loop) for ip in ips]
    return await asyncio.gather(*tasks)



def update_ip_statuses():
    ips = Ipmanzil.objects.all()
    ip_list = [ip.ip_manzili for ip in ips]
    results = asyncio.run(ping_all(ip_list))
    for ip, status in results:
        Ipmanzil.objects.filter(ip_manzili=ip).update(is_active=status)


# def update_gats_status1():
#     ips1 = GATS.objects.all()
#     ip_list1 = [ip1.ip_manzili for ip1 in ips1]
#     results1 = asyncio.run(ping_all(ip_list1))
#     for ip, status in results1:
#         GATS.objects.filter(ip_manzili=ip).update(is_active=status)

        # obj = Ipmanzil.objects.get(ip_manzili=ip).hudud
        # obj.is_active = status
        # obj.save()








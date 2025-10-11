import os

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

from accounts.forms import LoginForm, TadbirForm
from accounts.models import ChatMessage, Tadbir


# --------------------------- LOGIN VIEW ---------------------------
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            password = data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    return render(
                        request,
                        'account/login.html',
                        {'info': 'Foydalanuvchi aktiv emas', 'form': LoginForm()}
                    )
            else:
                return render(
                    request,
                    'account/login.html',
                    {'info': 'Login yoki parol xato kiritildi', 'form': LoginForm()}
                )
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


# --------------------------- TADBIR VIEW ---------------------------
@login_required
def tadbir(request):
    # POST bo‘lsa — tahrir yoki yangi yaratish holatini aniqlaymiz
    if request.method == "POST":

        # 🔹 1) Tahrirlash (update) qismi
        if 'edit_tadbir' in request.POST:
            pk = request.POST.get('tadbir_id')
            tadbir = get_object_or_404(Tadbir, pk=pk, user=request.user)

            # Formadagi ma'lumotlarni olish
            tadbir.nomi = request.POST.get('nomi')
            tadbir.aloqa_t = request.POST.get('aloqa_t')
            tadbir.h_qism = request.POST.get('h_qism')
            tadbir.izoh = request.POST.get('izoh')
            tadbir.asosiy_q = request.POST.get('asosiy_q')

            # Agar yangi fayl kiritilgan bo‘lsa
            if 'fayl' in request.FILES:
                tadbir.fayl = request.FILES['fayl']

            tadbir.save()
            messages.success(request, "✏️ Tadbir muvaffaqiyatli yangilandi!")
            return redirect('tadbir')

        # 🔹 2) Yangi tadbir yaratish
        else:
            image = request.FILES.get('fayl')
            form = TadbirForm(data=request.POST)
            if form.is_valid():
                new_tadbir = form.save(commit=False)
                new_tadbir.user = request.user
                new_tadbir.fayl = image
                new_tadbir.save()
                messages.success(request, "✅ Tadbir muvaffaqiyatli yaratildi!")
                return redirect('tadbir')
            else:
                messages.error(request, "⚠️ Forma noto‘g‘ri to‘ldirilgan!")

    # GET — sahifani ko‘rsatish
    form = TadbirForm()
    context = {
        'form': form,
        'tadbirlar': Tadbir.objects.filter(user=request.user).order_by('-id')
    }
    return render(request, 'tadbir.html', context)


# --------------------------- PHONE VIEW ---------------------------
@login_required
def phone(request):
    return render(request, 'phone.html')


# --------------------------- CHAT VIEW ---------------------------
@login_required
def chat_view(request):
    users = User.objects.all()
    chat_messages = ChatMessage.objects.order_by('timestamp')
    return render(request, 'dashboard.html', {'users': users, 'chat_messages': chat_messages})


# --------------------------- SEND MESSAGE VIEW ---------------------------
@login_required
def send_message(request):
    if request.method == 'POST':
        msg = request.POST.get('message')
        video = request.FILES.get('video')
        image = request.FILES.get('image')

        if not msg or msg.strip() == "":
            messages.error(request, "Yuboriladigan ma'lumot kiritilmadi.")
            return redirect('dashboard')

        # Fayl hajmi cheklovi (10 MB)
        if video and video.size > 10 * 1024 * 1024:
            messages.error(request, "Video hajmi 10 MB dan oshmasligi kerak.")
            return redirect('dashboard')

        # Fayl turi cheklovi
        ALLOWED_VIDEO_TYPES = ['.mp4', '.webm', '.mov']
        if video:
            ext = os.path.splitext(video.name)[1].lower()
            if ext not in ALLOWED_VIDEO_TYPES:
                messages.error(request, "Faqat mp4, webm yoki mov formatdagi videolar qabul qilinadi.")
                return redirect('dashboard')

        ChatMessage.objects.create(
            sender=request.user,
            message=msg,
            video=video,
            image=image,
        )
        return redirect('dashboard')

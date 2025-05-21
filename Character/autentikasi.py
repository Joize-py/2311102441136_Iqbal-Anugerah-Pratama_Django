from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
 
def login_form(request):
    if request.user.is_authenticated:
        return redirect('karakteradmin')
    template_name = 'dashboard/login.html'
    pesan = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('karakteradmin')
        else:
            pesan = "gagal login"

    context = {
        'pesan': pesan,
    }
    return render(request, template_name, context)


def signup_form(request):
    if request.user.is_authenticated:
        redirect('karakteradmin')

    pesan = ''
    template_name = 'dashboard/signup.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        namadepan = request.POST.get('namadepan')
        namabelakang = request.POST.get('namabelakang')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        print(username, namadepan, namabelakang, email, password1, password2)

        if password1 == password2:
            check_user = User.objects.filter(username=username)
            if check_user.count() == 0:
                user = User.objects.create_user(
                    username=username,
                    first_name=namadepan,
                    last_name=namabelakang,
                    email=email,
                    password=password1,
                    is_active=True,
                )
                return redirect('karakteradmin')
            else:
                pesan = "Username sudah ada"
        else:
            pesan = "Password tidak sama"

       
    context = {
        'pesan': pesan,
    }
    return render(request, template_name, context)
    
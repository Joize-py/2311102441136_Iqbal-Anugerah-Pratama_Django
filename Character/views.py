from django.shortcuts import render, redirect
from django.http import HttpResponse
from Character.models import Karakter, Hero
from Character.forms import HeroForm




# Create your views here.


def karakteradmin(request):
    template_name = 'dashboard/karakteradmin.html'
    karakter = Karakter.objects.all()
    context = {
        'tittle': 'halaman karakter',
        'karakter': karakter
    }
    return render(request, 'dashboard/karakteradmin.html' , {'karakter' : karakter})


def karakteradd(request):
    template_name = 'dashboard/karakteradd.html'
    if request.method =="POST":
        nama = request.POST.get('name')
        roles = request.POST.get('role')
        difficulty = request.POST.get('difficulty')
        tier = request.POST.get('tier')

        Karakter.objects.create(
            name = nama,
            role = roles,
            difficulty = difficulty,
            tier = tier
        )
        return redirect ('karakter') 
    context = {
        'tittle': 'halaman karakteradd',
    
    }
    return render(request, template_name, context)


def karakterupdate(request, id):
    template_name = 'dashboard/karakterupdate.html'
    karakter = Karakter.objects.get(id=id)
    if request.method == "POST":
        nama = request.POST.get('name')
        roles = request.POST.get('role')
        difficulty = request.POST.get('difficulty')
        tier = request.POST.get('tier')

        karakter.name = nama
        karakter.role = roles
        karakter.difficulty = difficulty
        karakter.tier = tier
        karakter.save()
        return redirect ('karakter') 
    context = {
        'tittle': 'blog Page',
        'karakter': karakter,
    }
    return render(request, template_name, context)


def karakterdelete(request, id):
    Karakter.objects.get(id=id).delete()
    return redirect('karakter')


def dashboard(request):
    template_name = 'dashboard/dashboard.html'
    context = {
        'tittle': 'blog Page',
        'welcome': 'Welcome to blog Page',
    }
    return render(request, template_name, context)


def baseadmin(request):
    template_name = 'dashboard/baseadmin.html'
    context = {
        'tittle': 'Base Page',
        'welcome': 'Welcome to Base Page',
    }
    return render(request, template_name, context)


def login(request):
    template_name = 'dashboard/login.html'
    context = {
        'tittle': 'Base Page',
        'welcome': 'Welcome to Base Page',
    }
    return render(request, template_name, context)


def charadmin(request):
    template_name = 'dashboard/charadmin.html'
    char = Hero.objects.all()
    context = {
        'tittle' : 'Charkter',
        'char' : char
    }
    return render(request, 'dashboard/charadmin.html', {'char' : char})


def charadd(request):
    template_name = 'dashboard/charadd.html'
    if request.method == "POST":
        forms = HeroForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect ('charadmin')
        else:
            print(forms.errors_class)


    forms = HeroForm()
    context = {
        'tittle': 'halaman karakteradd',
        'forms': forms,
    }
    return render(request, template_name, context)


def charupdate(request, id):
    template_name = 'dashboard/charupdate.html'
    charupdate = Hero.objects.get(id=id)
    if request.method == "POST":
        forms = HeroForm(request.POST, request.FILES, instance=charupdate)
        if forms.is_valid():
            forms.save()
            return redirect ('charadmin')
        else:
            print(forms.errors_class)
    forms = HeroForm()
    context = {
        'tittle': 'blog Page',
        'forms': forms,
    }
    return render(request, template_name, context)


def chardelete(requst, id):
    Hero.objects.get(id=id).delete()
    return redirect ('char')

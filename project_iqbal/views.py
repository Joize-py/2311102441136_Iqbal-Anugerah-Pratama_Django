from django.shortcuts import render, redirect
from django.http import HttpResponse
from Character.models import Karakter, Hero


def home(request):
    template_name = 'halaman/index.html'
    context = {
        'tittle' : 'my home',
        'welcome' : 'welcome my home',
    }
    return render(request, template_name, context)


def char(request):
    template_name = 'halaman/char.html'
    char = Hero.objects.all()
    context = {
        'tittle' : 'Charkter',
        'char' : char
    }
    return render(request, 'halaman/char.html', {'char' : char})


def contacts(request):
    template_name = 'halaman/contacts.html'
    context = {
        'tittle' : 'Contact',
        'welcome' : 'welcome my home',
    }
    return render(request, template_name, context)


def base(request):
    template_name = 'halaman/base.html'
    context = {
        'tittle': 'Base Page',
        'welcome': 'Welcome to Base Page',
    }
    return render(request, template_name, context)


def blog(request):
    template_name = 'halaman/blog.html'
    context = {
        'tittle': 'blog Page',
        'welcome': 'Welcome to blog Page',
    }
    return render(request, template_name, context)


def detail(request):
    template_name = 'halaman/detail.html'
    context = {
        'tittle': 'blog Page',
        'welcome': 'Welcome to detail-blog Page',
    }
    return render(request, template_name, context)


def karakter(request):
    template_name = "halaman/karakter.html"
    karakter = Karakter.objects.all() 
    context = {
        'tittle': 'halaman karakter',
        'karakter': karakter
    }
    return render(request, 'halaman/karakter.html' , {'karakter' : karakter})


def map(request):
    template_name = 'halaman/map.html'
    context = {
        'tittle': 'blog Page',
        'welcome': 'Welcome to blog Page',
    }
    return render(request, template_name, context)

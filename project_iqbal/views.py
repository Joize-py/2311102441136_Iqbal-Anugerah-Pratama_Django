from django.shortcuts import render, redirect
from django.http import HttpResponse
from Character.models import Karakter
def home(request):
    template_name = 'halaman/base.html'
    context = {
        'tittle' : 'my home',
        'welcome' : 'welcome my home',
    }
    return render(request, template_name, context)

def char(request):
    template_name = 'halaman/char.html'
    context = {
        'tittle' : 'Charkter',
        'welcome' : 'welcome my home',
    }
    return render(request, template_name, context)

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

def karakteradd(request):
    template_name = "halaman/karakteradd.html"
    if request.method =="POST":
        nama = request.POST.get('name')
        roles = request.POST.get('role')
        difficulty = request.POST.get('difficulty')
        description = request.POST.get('description')

        Karakter.objects.create(
            name = nama,
            role = roles,
            difficulty = difficulty,
            description = description
        )
        return redirect ('karakter') 
    context = {
        'tittle': 'halaman karakteradd',
    
    }
    return render(request, template_name, context)

def karakterupdate(request, id):
    template_name = 'halaman/karakterupdate.html'
    karakter = Karakter.objects.get(id=id)
    if request.method == "POST":
        nama = request.POST.get('name')
        roles = request.POST.get('role')
        difficulty = request.POST.get('difficulty')
        description = request.POST.get('description')
        karakter.name = nama
        karakter.role = roles
        karakter.difficulty = difficulty
        karakter.description = description
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


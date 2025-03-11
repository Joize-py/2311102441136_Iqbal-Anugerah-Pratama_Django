from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    template_name = 'home.html'
    context = {
        'tittle' : 'my home',
        'welcome' : 'welcome my home',
    }
    return render(request, template_name, context)

def about(request):
    template_name = 'about.html'
    context = {
        'tittle' : 'about me',
        'welcome' : 'ini page about',
    }
    return render(request, template_name, context)
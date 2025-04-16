from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    template_name = 'halaman/base.html'
    context = {
        'tittle' : 'my home',
        'welcome' : 'welcome my home',
    }
    return render(request, template_name, context)
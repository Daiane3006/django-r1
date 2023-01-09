from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'recipes/pages/home.html', context={'name': 'Daiane Correia'})

def sobre(request):
    return HttpResponse('SOBRE - hello django')

def contato(request):
    return HttpResponse('CONTATO - hello django')
# Create your views here.

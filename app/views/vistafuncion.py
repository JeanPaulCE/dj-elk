from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'app/index.html')

def acerca_de(request):
    return render(request,'app/acerca-de.html')

def portafolio(request):
    return render(request,'app/portafolio.html')

def iniciar_sesion(request):
    return render(request,'app/iniciar-sesion.html')
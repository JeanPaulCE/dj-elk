from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.contrib.auth.models import User
from app.models import Cotizaciones, Perfil


def index(request):
    return render(request, 'app/index.html')


def acerca_de(request):
    return render(request, 'app/acerca-de.html')


def portafolio(request):
    return render(request, 'app/portafolio.html')

def usuario(request):

    auth_user = User.objects.get(username=request.user.username)
    fullname = auth_user.first_name+" "+auth_user.last_name
    try:
        perfil = Perfil.objects.get(usuario_id=request.user.id)
    except:
        perfil = None
    try:
        cotizaciones = list(Cotizaciones.objects.filter(solicitante_id=auth_user.id))
    except:
        cotizaciones = None

    context= {
        'perfil':perfil,
        'usuario':request.user.username,
        'fullname':fullname,
        'email':auth_user.email,
        'inicio': auth_user.last_login,
        'cotizaciones':cotizaciones
    }
    return render(request, 'app/administración-usuario.html', context=context)

@user_passes_test(lambda x: x.has_perm('administracion'))
def administracion(request):

    auth_user = User.objects.get(username=request.user.username)
    fullname = auth_user.first_name + " " + auth_user.last_name
    try:
        perfil = Perfil.objects.get(usuario_id=request.user.id)
    except:
        perfil = None

    try:
        cotizaciones = list(Cotizaciones.objects.filter(status=0))
    except:
        cotizaciones = None

    context= {
        'perfil':perfil,
        'usuario':request.user.username,
        'fullname':fullname,
        'email':auth_user.email,
        'inicio': auth_user.last_login,
        "cotizaciones":cotizaciones
    }
    return render(request, 'app/administracion-admin.html', context=context)
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views.vistafuncion import *
from .views.vistagenerica import *
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', index, name='index'),
    path('acerca-de/', acerca_de, name='acerca-de'),
    path('portafolio/', portafolio, name='portafolio'),
    path('usuario/', login_required(usuario), name='usuario'),
    path('registro/', RegistroCreateView.as_view(), name="registro"),
    path('accounts/login/', LoginView.as_view(template_name='app/iniciar-sesion.html'), name='iniciar-sesion'),
    path('cerrar-sesion/', LogoutView.as_view(template_name='app/cerrar-sesion.html'), name='cerrar-sesion'),
]

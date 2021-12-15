from django.urls import path

from .views.vistafuncion import *
from .views.vistagenerica import *

urlpatterns = [
    path('', index, name='index'),
    path('acerca-de/', acerca_de, name='acerca-de'),
    path('portafolio/', portafolio, name='portafolio'),
    path('iniciar-sesion/', iniciar_sesion, name='iniciar-sesion'),
    path('registro/', RegistroCreateView.as_view(), name="registro"),
]

from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView #, UpdateView, DeletView
from app.forms import UsuariosForm


class RegistroCreateView(CreateView):
    model = User
    form_class = UsuariosForm
    template_name = "app/registro.html"
    success_url = reverse_lazy('iniciar-sesion')

# class crearCotizacion(DeletView):
#     model = Cotizaciones
#
# class editarCotizacion(UpdateView):
#     model = Cotizaciones
#
# class crearCotizacion(CreateView):
#     model = Cotizaciones

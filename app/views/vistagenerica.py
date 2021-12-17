from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView #, UpdateView, DeletView
from app.forms import UsuariosForm, CotizacionesFormulario
from app.models import Cotizaciones


class RegistroCreateView(CreateView):
    model = User
    form_class = UsuariosForm
    template_name = "app/registro.html"
    success_url = reverse_lazy('iniciar-sesion')


class RegistroCotizacion(CreateView):
    model = Cotizaciones
    fields = ['titulo','descripcion','servicio']
    template_name = "app/cotizaciones.html"
    success_url = reverse_lazy('usuario')
    def form_valid(self, form):
        status = 0
        solicitante_id = self.request.user.id
        form.instance.status = status
        form.instance.solicitante_id = solicitante_id
        return super(RegistroCotizacion, self).form_valid(form)


# class crearCotizacion(DeletView):
#     model = Cotizaciones
#
# class editarCotizacion(UpdateView):
#     model = Cotizaciones
#
# class crearCotizacion(CreateView):
#     model = Cotizaciones

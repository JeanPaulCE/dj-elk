from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView  # , UpdateView, DeletView
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

class EditarCotizacion(UserPassesTestMixin,UpdateView):
    model = Cotizaciones
    fields = ['titulo','descripcion','servicio']
    template_name = "app/cotizaciones.html"
    success_url = reverse_lazy('usuario')
    def test_func(self):
        existente = Cotizaciones.objects.get(id=self.kwargs['pk'])
        return existente.solicitante.pk == self.request.user.id

class AceptarCotizacion(UserPassesTestMixin,UpdateView):
    model = Cotizaciones
    fields = []
    template_name = "app/Aceptar_cotizaciones.html"
    success_url = reverse_lazy('administracion')
    def form_valid(self, form):
        form.instance.status = '1'
        return super(AceptarCotizacion, self).form_valid(form)
    def test_func(self):
        return self.request.user.has_perm('app.administracion')

class RechazarCotizacion(UserPassesTestMixin,UpdateView):
    model = Cotizaciones
    fields = []
    template_name = "app/rechazar_cotizaciones.html"
    success_url = reverse_lazy('administracion')
    def form_valid(self, form):
        form.instance.status = '2'
        return super(RechazarCotizacion, self).form_valid(form)
    def test_func(self):
        return self.request.user.has_perm('app.administracion')



# class crearCotizacion(DeletView):
#     model = Cotizaciones
#
# class editarCotizacion(UpdateView):
#     model = Cotizaciones
#
# class crearCotizacion(CreateView):
#     model = Cotizaciones

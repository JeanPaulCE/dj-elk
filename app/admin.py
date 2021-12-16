from django.contrib import admin

# Register your models here.
from app.models import Servicios, Perfil, Tareas

admin.site.register(Servicios)
admin.site.register(Perfil)
admin.site.register(Tareas)


from django.contrib import admin

# Register your models here.
# admin.py

from django.contrib import admin
from .models import Cliente, Contacto, Direccion, Compra, Servicio, Subservicio, Trabajador, Componente, RealizarCompra, CompraSubservicio, ServicioSubservicio, SubservicioComponente, PagoSalario

admin.site.register(Cliente)
admin.site.register(Contacto)
admin.site.register(Direccion)
admin.site.register(Compra)
admin.site.register(Servicio)
admin.site.register(Subservicio)
admin.site.register(Trabajador)
admin.site.register(Componente)
admin.site.register(RealizarCompra)
admin.site.register(CompraSubservicio)
admin.site.register(ServicioSubservicio)
admin.site.register(SubservicioComponente)
admin.site.register(PagoSalario)


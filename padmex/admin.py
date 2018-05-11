from django.contrib import admin
from .models import Cliente, Producto, Pedido, Detalle, Cita

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(Detalle)
admin.site.register(Cita)

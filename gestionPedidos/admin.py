from django.contrib import admin

from gestionPedidos.models import *

# Register your models here.

#PANEL DE ADMINISTRACION

class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","telefono")
    search_fields=("nombre",)
    
    

class ArticulosAdmin(admin.ModelAdmin):
    list_display=("nombre","seccion","precio")
    search_fields=("nombre","seccion")
    list_filter=("seccion",)

class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero","fecha","entregado")
    list_filter=("entregado","fecha")
    search_fields=("numero",)
    date_hierarchy=("fecha")

admin.site.register(Clientes, ClientesAdmin)

admin.site.register(Articulos,ArticulosAdmin)

admin.site.register(Pedidos, PedidosAdmin)
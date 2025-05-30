from django.shortcuts import render
from django.http import *
from gestionPedidos.models import Articulos
from TiendaOnline import settings
from django.core.mail import send_mail
from gestionPedidos.forms import FormularioContacto

# Create your views here.

def busqueda_productos(request):

    return render(request, "Busqueda_Productos.html")

def buscar(request):

    if request.GET["prd"]:

        #mensaje="Artículo buscado: {}".format(request.GET["prd"])
        producto=request.GET["prd"]

        if len(producto)>20:
            mensaje="Texto de búsqueda demasiado largo"
        else:
            articulos=Articulos.objects.filter(nombre__icontains=producto)

            return render(request, "resultados_busqueda.html",{"articulos":articulos,"query":producto})

    else: mensaje="No has introducido nada"


    
    return HttpResponse(mensaje)

def contacto(request):

    if request.method=="POST":

        miFormulario=FormularioContacto(request.POST)

        if miFormulario.is_valid():

            infForm=miFormulario.cleaned_data()

            send_mail(infForm['asunto'], infForm['mensaje'], infForm.get('email',''),['<insert email>'])

            return render(request, "gracias.html")
        
    else: miFormulario=FormularioContacto()

    return render(request, "formulario.html", {"form":miFormulario})



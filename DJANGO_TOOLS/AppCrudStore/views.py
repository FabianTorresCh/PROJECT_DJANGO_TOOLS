#VISTA DE APLICACION

# IMPORTACION DE BIBLIOTECAS
from django.shortcuts import render
from django.http import HttpResponse



# VISTA DE INICIO
def DefView(request):
    return HttpResponse("<h1>MENSAJE DE INICIO</h1>")


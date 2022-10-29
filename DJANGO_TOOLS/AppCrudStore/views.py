#VISTA DE APLICACION

# IMPORTACION DE BIBLIOTECAS
from django.shortcuts import render
from django.http import HttpResponse


# VISTA DE INICIO
def DefViewHome(request):
    return render(request,"Template_Main/ViewHome.html")

# VISTA DE NOSOTROS
def DefViewAboutUs(request):
    return render(request,"Template_Main/ViewAboutUs.html")

# VISTA DE CRUD INDEX
def DefViewCrudIndex(request):
    return render(request,"Template_Crud/CrudIndex.html")

# VISTA DE CRUD EDIT
def DefViewCrudEdit(request):
    return render(request,"Template_Crud/CrudEdit.html")

# VISTA DE CRUD CREATE
def DefViewCrudCreate(request):
    return render(request,"Template_Crud/CrudCreate.html")




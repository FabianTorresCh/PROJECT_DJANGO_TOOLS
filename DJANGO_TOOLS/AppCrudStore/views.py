#VISTA DE APLICACION

# IMPORTACION DE BIBLIOTECAS
from django.shortcuts import render
from django.http import HttpResponse
# IMPORTACION DE MODELOS
from AppCrudStore.models import ClassProduct
# IMPORTACION DE FORMULARIO
from AppCrudStore.Forms import ClassFormProduct


# ---------------------------------------------------------
# VERIFICACION DE IMPORTACION DE ELEMENTOS

print("\n>>>IMPORTACION DE ELEMTNOS")
print("ClassProduct: [",ClassProduct,"]"," / Tipo: [",type(ClassProduct),"]\n"
     "ClassFormProduct: [",ClassFormProduct,"]"," / Tipo: [",type(ClassFormProduct),"]\n")



# ---------------------------------------------------------
# VISTA DE INICIO
def DefViewHome(request):

    # !!! NOTIFICACION
    print("\n>>> VIEW HOME\n")

    return render(request,"Template_Main/ViewHome.html")


# ---------------------------------------------------------
# VISTA DE NOSOTROS
def DefViewAboutUs(request):

    # !!! NOTIFICACION
    print("\n>>> VIEW ABOUT US\n")

    return render(request,"Template_Main/ViewAboutUs.html")


# ---------------------------------------------------------
# VISTA DE CRUD INDEX
def DefViewCrudIndex(request):

    # !!! NOTIFICACION
    print("\n>>> VIEW INDEX\n")

    # ELEMENTOS DE INTERACION PARA EL HTML
    ModelClassProduct = ClassProduct.objects.all()

    # MENSAJE DE VERIFICACION DE USO DE MODELO
    print("\n>>> USO DE MODELO PRODUCTO: ",ModelClassProduct)

    # SE ENVIA VARIABLE
    return render(request,"Template_Crud/CrudIndex.html",{'Products_All':ModelClassProduct})


# ---------------------------------------------------------
# VISTA DE CRUD EDIT
def DefViewCrudEdit(request):
    return render(request,"Template_Crud/CrudEdit.html")


# ---------------------------------------------------------
# VISTA DE CRUD CREATE
def DefViewCrudCreate(request):

    # OBJETO FORMULARIO
    print("\n>>> APERTURA DE FORMULARIO DE PRODUCTOS\n")
    ObjForm = ClassFormProduct(request.POST or None)
    print("\n>>> CIERRE DE FORMULARIO DE PRODUCTOS\n")

    return render(request,"Template_Crud/CrudCreate.html", {'ObjForm_Html':ObjForm})




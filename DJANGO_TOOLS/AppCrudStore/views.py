#VISTA DE APLICACION

# IMPORTACION DE BIBLIOTECAS
from django.shortcuts import render, redirect
from django.http import HttpResponse
# IMPORTACION DE MODELOS
from AppCrudStore.models import ClassProduct
# IMPORTACION DE FORMULARIO
from AppCrudStore.Forms import ClassFormProduct

# ---------------------------------------------------------
print("\n>>> OPEN view.py")

# ---------------------------------------------------------
# VERIFICACION DE IMPORTACION DE ELEMENTOS

print("\n>>>IMPORTACION DE ELEMTNOS")
print("ClassProduct: [",ClassProduct,"]"," / Tipo: [",type(ClassProduct),"]\n"
     "ClassFormProduct: [",ClassFormProduct,"]"," / Tipo: [",type(ClassFormProduct),"]\n")


# ---------------------------------------------------------
# VISTA DE INICIO
def DefViewHome(request):

    # !!! NOTIFICACION
    print("\n>>> DefViewHome\n")
    return render(request,"Template_Main/ViewHome.html")


# ---------------------------------------------------------
# VISTA DE NOSOTROS
def DefViewAboutUs(request):

    # !!! NOTIFICACION
    print("\n>>> DefViewAboutUs\n")
    return render(request,"Template_Main/ViewAboutUs.html")


# ---------------------------------------------------------
# VISTA DE CRUD INDEX
def DefViewCrudIndex(request):

    # !!! NOTIFICACION
    print("\n>>> DefViewCrudIndex\n")

    # ELEMENTOS DE INTERACION PARA EL HTML
    ModelClassProduct = ClassProduct.objects.all()

    # MENSAJE DE VERIFICACION DE USO DE MODELO
    print("\n>>> USO DE MODELO PRODUCTO: ",ModelClassProduct)

    # SE ENVIA VARIABLE
    return render(request,"Template_Crud/CrudIndex.html",{'Products_All':ModelClassProduct})


# ---------------------------------------------------------
# VISTA DE CRUD EDIT
# SE MODIFICA EL TIPO DE SOLICITUD DEL LA FUNCION VISTA, SE LE AGREGA LA VARIABLE VarProductId
def DefViewCrudEdit(request, VarProductId):

    # !!! NOTIFICACION
    print("\n>>> DefViewCrudEdit\n")
    # OBTIENE INFORMACION DE LA TABLA MODEL SEGUN EL ID
    ObjProductEdit = ClassProduct.objects.get(ProductId=VarProductId)
    #PASA LA INFORMACION DEL PRODUCTO SELECCIONADO AL FORMULARIO
    ObjForm = ClassFormProduct(request.POST or None, request.FILES or None, instance=ObjProductEdit)
    # CONDICIONAL PARA EDITAR FORMULARIO
    if ObjForm.is_valid() and request.POST:
        ObjForm.save()
        print("\n>>> DefViewCrudEdit/EditForm_Save\n")
        return redirect('/UrlIncludeAppCrudStore/UrlAppCrudStore_Index/')
    else:
        print("")
    return render(request,"Template_Crud/CrudEdit.html", {'ObjForm_Html':ObjForm})


# ---------------------------------------------------------
# VISTA DE CRUD CREATE
def DefViewCrudCreate(request):

    # !!! NOTIFICACION
    print("\n>>> DefViewCrudCreate\n")

    # OBJETO FORMULARIO
    print("\n>>> APERTURA DE FORMULARIO DE PRODUCTOS\n")
    # SE ENVIA EL OBJETO TIPO FORMULARIO PARA LA INTERACCION EN LA VISTA
    ObjForm = ClassFormProduct(request.POST or None, request.FILES or None)
    print("\n>>> ObjForm: [",ObjForm,"]\n")

    print("\n>>> VALID ObjForm \n")
    if ObjForm.is_valid():
        ObjForm.save()
        print("\n>>> DefViewCrudCreate/ [VALID SAVE CORRECT ObjForm]\n")
        # EL METODO redirect, REDIRECCIONA AL USUARIO UNA VEZ REALIZADA LA ACCION
        return redirect('/UrlIncludeAppCrudStore/UrlAppCrudStore_Index/')
    else:
        print("\n>>> DefViewCrudCreate/ [VALID SAVE ERROR ObjForm]\n")

    return render(request,"Template_Crud/CrudCreate.html", {'ObjForm_Html':ObjForm})


# ---------------------------------------------------------
# VISTA DE CRUD DELETE
def DefViewDelete(request, VarProductId):

    # IDENTIFICAR OBJETO POR ID PARA ELIMINAR
    ObjProductDelate = ClassProduct.objects.get(ProductId=VarProductId)
    # ELIMINACION DE ELEMENTO
    ObjProductDelate.delete()
    return redirect('/UrlIncludeAppCrudStore/UrlAppCrudStore_Index/')
from django.contrib import admin
from django.urls import path

# CONFIGURACION PARA VISUALIZACION DE ELEMENTOS IMAGENES
from django.conf import settings
from django.contrib.staticfiles.urls import static
# IMPORTACION DE VISTAS
from AppCrudStore.views import \
    DefViewHome, \
    DefViewAboutUs, \
    DefViewCrudIndex, \
    DefViewCrudEdit, \
    DefViewCrudCreate

# !!! NOTIFICACION
print("\n>>> URL´S AppCrudStore\n")

urlpatterns = [
    # DIRECCION TEMPLATE ADMIN
    path('UrlAdminAppCrudStore/', admin.site.urls),

    # DIRECCION TEMPLATE INICIO
    path('UrlAppCrudHome/', DefViewHome, name="Home"),

    # DIRECCION DE ABOUT US
    path('UrlAppCrudStore_AboutUs/', DefViewAboutUs, name="AboutUs"),

    # DIRECCION DE CRUD INDEX
    path('UrlAppCrudStore_Index/', DefViewCrudIndex, name="CrudIndex"),

    # DIRECCION DE CRUD EDIT
    path('UrlAppCrudStore_Edit/', DefViewCrudEdit, name="CrudEdit"),

    # DIRECCION DE CRUD CREATE
    path('UrlAppCrudStore_Create/', DefViewCrudCreate, name="CrudCreate")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
""" ELEMENTO NECESARIO PARA VISUALIZACION DE ELEMENTOS
** static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) **
"""
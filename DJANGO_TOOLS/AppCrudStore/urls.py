from django.contrib import admin
from django.urls import path
from AppCrudStore.views import \
    DefViewHome, \
    DefViewAboutUs, \
    DefViewCrudIndex, \
    DefViewCrudEdit, \
    DefViewCrudCreate

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





]

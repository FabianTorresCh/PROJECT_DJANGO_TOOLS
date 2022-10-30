from django.contrib import admin
# IMPORTACION DE MODELO
from AppCrudStore.models import ClassProduct

# -------------------------------------------------
# Permite la manipuacion de las base de datos por el administrador y demas usuarios

# -------------------------------------------------
# METODO DE VISUALIZACION DE ELEMNTOS

class ViewClassProduct(admin.ModelAdmin):
    list_display = ("ProductId","ProductName","ProductDescription","ProductValue","ProductInventory","ProductImage")
    search_fields = ("ProductId","ProductName")
    list_filter = ("ProductId","ProductName","ProductValue","ProductInventory",)




# -------------------------------------------------
# REGISTRO DE MODELO DE PRODUCTO

# MODELO DE PRODUCTOS
admin.site.register(ClassProduct,ViewClassProduct)
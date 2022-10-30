from django.db import models

# ---------------------------------------------------------
# MODELS PRODUCTS

# SE DEFINE COMO ESTRUCTURA DE LA TABLA
# LAS CLASES CREADAS DEBEN TENER EL INDICATIVO DE **TABLE**
class ClassProduct(models.Model):
    ProductId = models.AutoField(primary_key=True, verbose_name="Codigo")
    ProductName = models.CharField(max_length=50, verbose_name="Nombre")
    ProductDescription = models.TextField(null=True, verbose_name="Descripcion")
    ProductValue = models.FloatField(verbose_name="Valor")
    ProductInventory = models.IntegerField(verbose_name="Inventario")
    ProductImage = models.ImageField(upload_to="Images/",null=True, verbose_name="Imagen")

    # METODO PARA BORRADO DE IMAGEN
    def DefDeleteImage(self, using = None, keep_parents=False):
        self.ProductImage.storage.delete(self.ProductImage.name)
        super(). delete()
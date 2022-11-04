# ESTE ELEMENTO FUE CREADO POR ERROR

# IMPORTACION DE FORMULARIO DE DJANGO
from django import forms
# IMPORTACION DE OBJETO O MODELO DE MANIPULACION DE FORMULARIO
from AppCrudStore.models import ClassProduct


class ClassFormProduct(forms.ModelForm):
    class Meta:
        model = ClassProduct
        fields = '__all__'
from django import forms
from AppCrudStore.models import ClassProduct

# ---------------------------------------------------------
print("\n>>> OPEN Forms.py")

print("\n>>>IMPORTACION DE ELEMTNOS")
print("ClassProduct: [",ClassProduct,"]"," / Tipo: [",type(ClassProduct),"]\n")


class ClassFormProduct(forms.ModelForm):
    print("\n>>> ClassFormProduct\n")
    class Meta:
        model = ClassProduct
        fields = '__all__'
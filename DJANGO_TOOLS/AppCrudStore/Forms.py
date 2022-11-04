from django import forms
from AppCrudStore.models import ClassProduct


class ClassFormProduct(forms.ModelForm):
    print("\n>>> ClassFormProduct\n")
    class Meta:
        model = ClassProduct
        fields = '__all__'
from django import forms

class FamiliarForm(forms.Form):
    nombre= forms.CharField(max_length=40) #campo de texto
    apellido= forms.CharField(max_length=40) #campo de enteros
    fecha_nacimiento= forms.DateField()
    anios=forms.IntegerField()

class NegociosForm(forms.Form):
    nombre1= forms.CharField(max_length=40)
    provincia= forms.CharField(max_length=40)
    pais= forms.CharField(max_length=40)
    telefono= forms.IntegerField()

class InmobiliariosForm(forms.Form):
    direccion= forms.CharField(max_length=60)
    localidad= forms.CharField(max_length=40)
    mt2= forms.IntegerField()

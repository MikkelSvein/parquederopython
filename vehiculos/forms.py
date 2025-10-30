from django import forms
from .models import Vehiculo
class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['placa','nombre','documento','tipo']

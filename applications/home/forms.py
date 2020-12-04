from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):
    
    class Meta:
        model = Prueba
        # fields = ('__all__')
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',
        )
        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'placeholder': 'Ingrese Texto',
                    'class': 'form-control'
                } 
            )
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad'] #recupera la informacion de cantifdad que se envio por el dormulario
        if cantidad < 10:
            raise forms.ValidationError('La cantidad debe ser mayor a 10')
        return cantidad

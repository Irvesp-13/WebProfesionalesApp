# Vamos a crear formularios para cada modulo de la app/modulo

from .models import Modulo
from django import forms

# Crear una clase por cada formulario que necesitemos
class moduloForm(forms.ModelForm):
    # Definir los metadatos del formulario
    class Meta:
        # Personalizar el formulario

        # 1.- Definir el modelo
        model = Modulo

        # 2.- Definir los campos que deben aparecer
        fields = ['nombre', 'imagen']

        # 3.- Atributos de las etiquetas (widgets)
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del modulo'
                }
            ),
        }

        # 4.- Personalizar las etiquetas
        labels = {
            'nombre': 'Nombre del modulo',
            'imagen': 'URL de la imagen'
        }

        # 5.- Personalizar los mensajes de error
        error_messages = {
            'nombre': {
                'required': 'Este campo es obligatorio',
                'invalid': 'El valor ingresado no es válido'
            },
        }
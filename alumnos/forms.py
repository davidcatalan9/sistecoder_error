from . import models
from django.forms import ModelForm

class AlumnosForm(ModelForm):
    class Meta:
        model = models.Alumnos
        fields = ['rut', 'nombre', 'apellido', 'direccion', 'curso' ]
        
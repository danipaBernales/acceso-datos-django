from django import forms
from .models import Tarea, Etiqueta, Prioridad

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ('titulo', 'descripcion', 'fecha_vencimiento', 'estado', 'etiqueta', 'prioridad', 'usuario_asignado')
         widgets = {
            'fecha_vencimiento': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'estado': forms.Select(choices=Tarea.ESTADO_CHOICES),
            'etiqueta': forms.Select(),
            'prioridad': forms.Select(),
            'usuario_asignado': forms.Select(),
        }

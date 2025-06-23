from django import forms
from .models import Evaluacion

class EvaluacionForm(forms.ModelForm):
    class Meta:
        model = Evaluacion
        fields = ['categoria', 'comentarios', 'nota']
from django import forms
from.models import Persona

class PersonaForm(forms.ModelForm):
    
    class meta:
        model = Persona
        fields = ["NOMBRE"]
import email
from django import forms
from .models import Comentario

 


class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ["nombre", "email" ,"telefono", "comentario"]
        #fields = '__all__'


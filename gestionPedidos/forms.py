from django import forms

class FormularioContacto(forms.Form):

    asunto=forms.CharField()
    email=forms.EmailField()
    comentario=forms.CharField()
from django import forms

class UsuarioForm(forms.Form):

    nombre = forms.CharField(label='Nombre', max_length=100, required=True)
    apellido = forms.CharField(label='Apellido', max_length=100, required=True)
    usuario = forms.CharField(label='Nombre de usuario', required=True)
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput)
    clave = forms.CharField(label='Clave', required=True, widget=forms.PasswordInput)
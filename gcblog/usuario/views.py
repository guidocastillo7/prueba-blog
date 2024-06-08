from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .forms import UsuarioForm

# Create your views here.

def registro(request):

    frm = UsuarioForm()

    context = {
        'frm':frm
    }

    return render(request, 'usuario/registro.html', context)


def saveUsuario(request):

    if request.method == 'POST':
        frm = UsuarioForm(request.POST)

        if frm.is_valid():
            data = frm.cleaned_data

            #Forma correcta de crear un usuario, pq asi encripta la clave y puedo poner los datos q quiera con el forms

            nuevoUsuario = User.objects.create_user(username=data["usuario"], email=data["email"], password=data["clave"])
            nuevoUsuario.first_name = data["nombre"]
            nuevoUsuario.last_name = data["apellido"]
            nuevoUsuario.save()



    return redirect('/')





'''class Registro(View):

    def get(self, request):
        form = UserCreationForm()

        context = {
            "form": form
        }

        return render(request, 'usuario/registro.html', context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        usuario = form.save()

        return redirect('/')'''
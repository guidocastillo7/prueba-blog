from django.shortcuts import render, redirect 

from .models import Articulo, Comentario

# Create your views here.

#Aqui quiero poner el inicio donde estan los articulos pa elegir
def index(request):

    objeto = Articulo.objects.all()

    context = {
        "contenido":objeto
    }
    
    return render(request, 'blog/index.html', context)

#Aqui quiero poner ya el articulo elegido
def contenido(request, el_id):

    objeto = Articulo.objects.get(pk=el_id)

    listaComentarios = Comentario.objects.filter(articulo=objeto)

    context ={
        "contenido":objeto,
        "comentarios":listaComentarios
    }
    
    return render(request, 'blog/contenido.html', context)


def comentar(request, articulo_id):

    if request.method == 'POST':

        obj = Articulo.objects.get(pk=articulo_id)

        coment = request.POST['comentario']
        if request.POST['name'] == '':
            name = 'anonimo'
        else:
            name = request.POST['name']

        newComent = Comentario()
        newComent.texto = coment 
        newComent.articulo = obj
        newComent.autor = name 
        newComent.save()

    return redirect('/contenido/' + str(articulo_id))
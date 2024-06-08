from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index),
    path('contenido/<int:el_id>', views.contenido, name= 'contenido'),
    path('comentar/<int:articulo_id>', views.comentar, name='comentar')
]
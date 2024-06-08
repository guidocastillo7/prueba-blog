from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Articulo(models.Model):

    titulo = models.CharField(max_length=150)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='imagenes')
    autor = models.ForeignKey(User, on_delete=models.RESTRICT)

    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):

    articulo = models.ForeignKey(Articulo, on_delete=models.RESTRICT)
    texto = models.TextField(default='')
    autor = models.CharField(max_length=100, default='anonimo')

    def __str__(self):
        return self.autor
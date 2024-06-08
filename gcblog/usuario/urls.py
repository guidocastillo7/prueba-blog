from django.urls import path 

from . import views
#from .views import Registro


urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('saveUsuario/', views.saveUsuario, name='saveUsuario')
]
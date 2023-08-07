from django.urls import path
from . import views


app_name = 'alumnos'
urlpatterns = [
    path( '', views.index, name='index' ),
    path( 'formulario', views.formulario, name='formulario'), 
    path( 'detalle/<int:alumno_id>', views.detalle, name='listaAlum' )
        
]






from django.urls import path
from . import views

app_name = 'cursos'
urlpatterns = [
    path( 'listaCursos', views.listaCursos, name='listaCursos'),
    path("detalleCurso/", views.detalleCurso, name="detalleCurso")
]


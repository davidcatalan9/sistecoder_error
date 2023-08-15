from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
import trabajos

from profesores.models import Trabajos



def listaTrabajos(request):
    TrabajosLis = Trabajos.objects.all()
    
    return render(
        request, 
        'listaTrabajos.html',
        context={'trabajos':TrabajosLis}
    )
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

import alumnos

from .forms import AlumnosForm

from .models import Alumnos
# Create your views here.
 
 


def index(request):
    AlumnosData = Alumnos.objects.all()
    
  
    return render(
        request,
        'listaAlum.html',
        context={'alumnos':AlumnosData }
    )
    
    
def detalle( request, alumnos_id ):
    alumnosd = get_object_or_404(Alumnos, id=alumnos_id)
    
    # alumnosd = Alumnos.objects.get(id=alumnos_id)
    
    import pdb ; pdb.set_trace()
    print( alumnosd) 
    return render(
        request, 'detalle.html',
        context={'alumnos':alumnosd}
        )
   
   
def formulario(request):
    if request.method == 'POST':
        form = AlumnosForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/alumnos')
        else:
            form = AlumnosForm()
    else:
        form = AlumnosForm()
        
    return render(
        request, 'alumnos_form.html', {'form': form }
    )
    
    
""" def formulario(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/profesores')
    else:
        form = ProfesorForm()
             
    return render(
        request, 'profesor_form.html', {'form': form} 
    ) """
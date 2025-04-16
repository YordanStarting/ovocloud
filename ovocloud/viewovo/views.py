from django.shortcuts import render
from django.http import HttpResponse
from .models import Viewovo
from .froms import ovoform
# Create your views her

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

# complaints views here 

def complaints(request):
    complaints = Viewovo.objects.all()
    print(complaints)
    return render(request, 'complaints/index.html', {'complaints': complaints})

def createpqrs(request):
    formulario = ovoform(request.POST or None)
    return render(request, 'complaints/crear.html', {'formulario': formulario})

def editpqrs(request):
    return render(request, 'complaints/editar.html')


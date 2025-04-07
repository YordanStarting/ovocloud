from django.shortcuts import render
from django.http import HttpResponse
from .models import Viewovo
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
    return render(request, 'complaints/crear.html')

def editpqrs(request):
    return render(request, 'complaints/editar.html')
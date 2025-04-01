from django.shortcuts import render
from django.http import HttpResponse
# Create your views her

def inicio(request):
    return HttpResponse("Bienvenido a Ovoproductos")

def nosotros(request):
    return render(request, 'paginas/nosotros.html')
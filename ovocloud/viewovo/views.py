from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Viewovo, MonitoreoAgua
from .froms import ovoform, MonitoreoAguaForm
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

# complaints aqua here 

# CREAR
def crear_monitoreo(request):
    if request.method == 'POST':
        form = MonitoreoAguaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_monitoreos')
    else:
        form = MonitoreoAguaForm()
    return render(request, 'monitoreo/crear.html', {'form': form})

# LISTAR
def listar_monitoreos(request):
    fecha_filtro = request.GET.get('fecha')  # Obtiene el valor del input "fecha" si se envía

    if fecha_filtro:
        monitoreos = MonitoreoAgua.objects.filter(fecha=fecha_filtro)
    else:
        monitoreos = MonitoreoAgua.objects.all()

    return render(request, 'monitoreo/listar.html', {
        'monitoreos': monitoreos,
        'fecha_filtro': fecha_filtro  # Lo enviamos al template para mantener el valor seleccionado
    })

# ACTUALIZAR
def editar_monitoreo(request, pk):
    monitoreo = get_object_or_404(MonitoreoAgua, pk=pk)
    if request.method == 'POST':
        form = MonitoreoAguaForm(request.POST, instance=monitoreo)
        if form.is_valid():
            form.save()
            return redirect('listar_monitoreos')
    else:
        form = MonitoreoAguaForm(instance=monitoreo)
    return render(request, 'monitoreo/editar.html', {'form': form})

# ELIMINAR
def eliminar_monitoreo(request, pk):
    monitoreo = get_object_or_404(MonitoreoAgua, pk=pk)
    if request.method == 'POST':
        monitoreo.delete()
        return redirect('listar_monitoreos')
    return render(request, 'monitoreo/eliminar.html', {'monitoreo': monitoreo})

from django.template.loader import get_template
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Viewovo, MonitoreoAgua
from .froms import ovoform, MonitoreoAguaForm
from xhtml2pdf import pisa
from django.shortcuts import render
# Create your views her

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')


#vista de dashborad

def dashboard(request):
    return render(request, 'dashboard/index.html')

def formsshow(request):
    formularios = [
        {"nombre": "Monitoreo pH","area": "Calidad", "url": reverse('listar_monitoreos')},
        {"nombre": "Editar PQR","area": "Calidad", "url": reverse('editpqrs')},
        {"nombre": "Formulario 3","area": "Calidad", "url": reverse('listar_monitoreos')},
        # Agrega más dinámicamente si quieres
    ]
    return render(request, 'directlinks/forms_show.html', {"formularios": formularios})

# complaints views here 

def complaints(request):
    complaints = Viewovo.objects.all()
    print(complaints)
    return render(request, 'formularios/complaints/index.html', {'complaints': complaints})

def createpqrs(request):
    formulario = ovoform(request.POST or None)
    return render(request, 'formularios/complaints/crear.html', {'formulario': formulario})

def editpqrs(request):
    return render(request, 'formularios/complaints/editar.html')

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
    return render(request, 'formularios/monitoreo/crear.html', {'form': form})

# LISTAR


def listar_monitoreos(request):
    lote_filtro = request.GET.get('lote')  # <--- Nuevo filtro por lote

    if lote_filtro:
        monitoreos = MonitoreoAgua.objects.filter(lote__icontains=lote_filtro)
    else:
        monitoreos = MonitoreoAgua.objects.all()

    return render(request, 'formularios/monitoreo/listar.html', {
        'monitoreos': monitoreos,
        'lote_filtro': lote_filtro,
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
    return render(request, 'formularios/monitoreo/editar.html', {'form': form})

# ELIMINAR
def eliminar_monitoreo(request, pk):
    monitoreo = get_object_or_404(MonitoreoAgua, pk=pk)
    if request.method == 'POST':
        monitoreo.delete()
        return redirect('listar_monitoreos')
    return render(request, 'formularios/monitoreo/eliminar.html', {'monitoreo': monitoreo})

# Descargar Certificado
def exportar_monitoreo_pdf(request):
    monitoreos = MonitoreoAgua.objects.all()
    template_path = 'formularios/monitoreo/pdf_monitoreos.html'
    context = {'monitoreos': monitoreos}
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="monitoreos.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('Error al generar el PDF')
    return response


#listar Formularios 


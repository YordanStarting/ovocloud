from django.template.loader import get_template
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Viewovo, MonitoreoAgua, RegistroViaje
from .froms import ovoform, MonitoreoAguaForm, registroViajeForm
from xhtml2pdf import pisa
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views her

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')


#vista de dashborad

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'directlinks/login_view.html')

def logout_view(request):
    logout(request)
    return redirect('login_view')

@login_required
def dashboard(request):
    return render(request, 'dashboard/index.html')

@login_required
def formsshow(request):
    formularios = [
        {"nombre": "Monitoreo pH","area": "Calidad", "url": reverse('listar_monitoreos')},
        {"nombre": "Editar PQR","area": "Calidad", "url": reverse('editpqrs')},
        {"nombre": "Registro Viajes","area": "Logistica", "url": reverse('listar_viaje')},
        # Agrega más dinámicamente si quieres
    ]
    return render(request, 'directlinks/forms_show.html', {"formularios": formularios})

# complaints views here 
@login_required
def complaints(request):
    complaints = Viewovo.objects.all()
    print(complaints)
    return render(request, 'formularios/complaints/index.html', {'complaints': complaints})
@login_required
def createpqrs(request):
    formulario = ovoform(request.POST or None)
    return render(request, 'formularios/complaints/crear.html', {'formulario': formulario})
@login_required
def editpqrs(request):
    return render(request, 'formularios/complaints/editar.html')

# complaints aqua here 

#####################################CRUD Monitoreo Agua#################################
# CREAR
@login_required
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
@login_required
def listar_monitoreos(request):
    fecha_filtro = request.GET.get('fecha')  # <--- Nuevo filtro por lote

    if fecha_filtro:
        monitoreos = MonitoreoAgua.objects.filter(fecha=fecha_filtro)
    else:
        monitoreos = MonitoreoAgua.objects.all()

    return render(request, 'formularios/monitoreo/listar.html', {
        'monitoreos': monitoreos,
        'fecha_filtro': fecha_filtro,
    })
# ACTUALIZAR
@login_required
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
@login_required
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



#####################################CRUD RegistroViaje#################################
# CREAR
@login_required
def crear_registroviaje(request):
    if request.method == 'POST':
        form = registroViajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_viaje')
    else:
        form = registroViajeForm()
    return render(request, 'formularios/registroviaje/crear.html', {'form': form})
# LISTAR
@login_required
def listar_registroviaje(request):
    fecha_filtro = request.GET.get('fecha')  # <--- Nuevo filtro por lote

    if fecha_filtro:
        registro = RegistroViaje.objects.filter(fecha=fecha_filtro)
    else:
        registro = RegistroViaje.objects.all()

    return render(request, 'formularios/registroviaje/listar.html', {
        'registro': registro,
        'conductor_filtro': fecha_filtro,
    })
# ACTUALIZAR
@login_required
def editar_registroviaje(request, pk):
    registro = get_object_or_404(RegistroViaje, pk=pk)
    if request.method == 'POST':
        form = registroViajeForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('listar_viaje')
    else:
        form = registroViajeForm(instance=registro)
    return render(request, 'formularios/registroviaje/editar.html', {'form': form})
# ELIMINAR
@login_required
def eliminar_registroviaje(request, pk):
    registro = get_object_or_404(RegistroViaje, pk=pk)
    if request.method == 'POST':
        registro.delete()
        return redirect('listar_viaje')
    return render(request, 'formularios/registroviaje/eliminar.html', {'registro': registro})


from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),


    # # URL for the complaints page
    path('pqrs', views.complaints, name='complaints'),
    path('createpqrs', views.createpqrs, name='createpqrs'),
    path('editpqrs', views.editpqrs, name='editpqrs'),
    # # URL for the complaints wather
    path('formularios/monitereo/', views.listar_monitoreos, name='listar_monitoreos'),
    path('nuevo/', views.crear_monitoreo, name='crear_monitoreo'),
    path('editar/<int:pk>/', views.editar_monitoreo, name='editar_monitoreo'),
    path('eliminar/<int:pk>/', views.eliminar_monitoreo, name='eliminar_monitoreo'),
    path('exportar_pdf/', views.exportar_monitoreo_pdf, name='exportar_pdf'),
    # # URL for the dashboard
    path('dashboard/', views.dashboard, name='admin_dashboard'),
    path('formsshow/', views.formsshow, name='formsshow'),
    path('login_view/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout'),
    # # URL for the viajes
    path('viajes/', views.listar_registroviaje, name='listar_viaje'),
    path('viajes/nuevo/', views.crear_registroviaje, name='crear_viaje'),
    path('viajes/editar/<int:pk>/', views.editar_registroviaje, name='editar_viaje'),
    path('viajes/eliminar/<int:pk>/', views.eliminar_registroviaje, name='eliminar_viaje'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

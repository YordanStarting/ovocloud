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
    path('monitereo/', views.listar_monitoreos, name='listar_monitoreos'),
    path('nuevo/', views.crear_monitoreo, name='crear_monitoreo'),
    path('editar/<int:pk>/', views.editar_monitoreo, name='editar_monitoreo'),
    path('eliminar/<int:pk>/', views.eliminar_monitoreo, name='eliminar_monitoreo'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

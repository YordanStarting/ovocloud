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
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

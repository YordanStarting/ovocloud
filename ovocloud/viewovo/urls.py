from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),


    # # URL for the complaints page
    path('pqrs', views.complaints, name='complaints'),
    path('createpqrs', views.createpqrs, name='createpqrs'),
    path('editpqrs', views.editpqrs, name='editpqrs'),
]

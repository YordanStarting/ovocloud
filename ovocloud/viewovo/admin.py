from django.contrib import admin
from .models import Viewovo
from .models import MonitoreoAgua
# Register your models here.
# para registrar el modelo en el admin de django
admin.site.register(Viewovo)
admin.site.register(MonitoreoAgua)
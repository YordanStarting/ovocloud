from django import forms
from .models import Viewovo, MonitoreoAgua

class ovoform(forms.ModelForm):
    class Meta:
        model = Viewovo
        fields = '__all__'
        
class MonitoreoAguaForm(forms.ModelForm):
    class Meta:
        model = MonitoreoAgua
        fields = '__all__'
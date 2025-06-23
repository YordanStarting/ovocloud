from django import forms
from .models import Viewovo, MonitoreoAgua, RegistroViaje

class ovoform(forms.ModelForm):
    class Meta:
        model = Viewovo
        fields = '__all__'
        
class MonitoreoAguaForm(forms.ModelForm):
    class Meta:
        model = MonitoreoAgua
        fields = '__all__'

class registroViajeForm(forms.ModelForm):
    class Meta:
        model = RegistroViaje
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'km_inicial': forms.NumberInput(attrs={'step': '0.001'}),
            'km_final': forms.NumberInput(attrs={'step': '0.001'}),
            'km': forms.NumberInput(attrs={'step': '0.001'}),
            'gal_acpm': forms.NumberInput(attrs={'step': '0.001'}),
        }
from django import forms
from .models import Viewovo

class ovoform(forms.ModelForm):
    class Meta:
        model = Viewovo
        fields = '__all__'
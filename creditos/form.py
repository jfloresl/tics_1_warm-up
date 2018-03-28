from django.forms import ModelForm
from creditos.models import Calculator

class formcalculator(ModelForm):
    class Meta:
        model = Calculator

from django import forms

class Regform(forms.Form):
   monto=forms.IntegerField(min_value=1000000, max_value=10000000,error_messages={'required': 'Ingreses el monto'})
   meses=forms.IntegerField(min_value=2, max_value=48,error_messages={'required': 'ingrese los meses'})
   seguro=forms.BooleanField(required=False)



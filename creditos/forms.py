from django import forms

class Regform(forms.Form):
   monto=forms.IntegerField(min_value=1000000, max_value=10000000)
   meses=forms.IntegerField(min_value=2, max_value=48)
   seguro=forms.BooleanField()

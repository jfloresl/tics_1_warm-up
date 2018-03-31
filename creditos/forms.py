from django import forms

class Regform(forms.Form):
   monto=forms.IntegerField()
   meses=forms.IntegerField()
   seguro=forms.BooleanField()

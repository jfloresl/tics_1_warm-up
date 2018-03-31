from django.shortcuts import render
from .forms import Regform
from .models import *


def post_list(request):
 #banco=Banco.objects.filter().order_by('cae')
 form=Regform(request.POST)
 #if form.is_valid():
 # form_dicc=form.cleaned_data
 # print (form_dicc.get('monto'))
 return render(request, 'creditos/index.html',{"form":form})

def listabancos(request):
 valor1=request.POST['monto']
 banco=Banco.objects.filter().order_by('cae')
 return render(request, 'creditos/index2.html',{'banco':banco})

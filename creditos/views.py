from django.shortcuts import render
from django.http.response import HttpResponse
from .models import *

def post_list(request):
 banco=Banco.objects.filter().order_by('cae')
 return render(request, 'creditos/index.html', {'banco':banco})
def calcular(request):
 form= formcalculator()
 if request.method == 'POST':
   mo=int(request.POST['monto'])
   me=int(request.POST['meses'])
   v=mo*me
   return HttpResponse(v)
 return render(request,'creditos/index.html', {'form':form} )


from django.shortcuts import render
from .forms import Regform
from .models import *


def post_list(request):
 #hace correr el formulario de forms.py
 form=Regform(request.POST)
 return render(request, 'creditos/index.html',{"form":form})

def listabancos(request):
 #valores del entregados por el formulario
 monto=int(request.POST.get('monto'))
 meses=int(request.POST.get('meses'))
 seguro=request.POST.get('seguro')
 #lista de gastos
 gastos=[]
 for i in range(1,11):
  gastos.append(Banco.objects.values_list('gastos',flat=True).order_by('cae').get(pk=i))
 seg=[]
 imp=[]
 #selecciona impuesto y seguro segun la cantidad de meses
 if meses>0 and meses<=12:
                for i in range(1,11):
                   imp.append(Banco.objects.values_list('im_1',flat=True).order_by('cae').get(pk=i))
                if seguro=="on":
                 for i in range(1,11):
                   seg.append(Banco.objects.values_list('seguro_1',flat=True).order_by('cae').get(pk=i))
                banco=Banco.objects.filter().order_by('cae')
 elif meses>=13 and meses<=23:
                for i in range(1,11):
                   imp.append(Banco.objects.values_list('im_2',flat=True).order_by('cae').get(pk=i))
                if seguro=="on":
                 for i in range(1,11):
                   seg.append(Banco.objects.values_list('seguro_2',flat=True).order_by('cae').get(pk=i))
                banco=Banco.objects.filter().order_by('cae')
 elif meses>=24 and meses<=36:
                for i in range(1,11):
                   imp.append(Banco.objects.values_list('im_3',flat=True).order_by('cae').get(pk=i))
                if seguro=="on":
                 for i in range(1,11):
                   seg.append(Banco.objects.values_list('seguro_3',flat=True).order_by('cae').get(pk=i))
                banco=Banco.objects.filter().order_by('cae')
 elif meses>=37 and meses<=48:
                 for i in range(1,11):
                   imp.append(Banco.objects.values_list('im_4',flat=True).order_by('cae').get(pk=i))
                 if seguro=="on":
                  for i in range(1,11):
                   seg.append(Banco.objects.values_list('seguro_4',flat=True).order_by('cae').get(pk=i))
                 banco=Banco.objects.filter().order_by('cae')
 elif meses<0 or meses>48:
                imp=-1
 #llamado a la funcion para calcular el ctc
 costo_total=[]
 for i in range(1,10):
  costo_total.append(Banco.ctc(float(meses),float(seg[i]),float(gastos[i]),float(imp[i]),monto))
 return render(request, 'creditos/index2.html',{'banco':banco,'costo_total':costo_total}) 


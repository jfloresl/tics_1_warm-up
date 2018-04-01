from django.shortcuts import render
from .forms import Regform
from .models import *


def post_list(request):
 form=Regform(request.POST)
 return render(request, 'creditos/index.html',{"form":form})

def listabancos(request):
 monto=int(request.POST.get('monto'))
 meses=int(request.POST.get('meses'))
 seguro=request.POST.get('seguro')
 gastos=[]
 for i in range(1,11):
  gastos.append(Banco.objects.values_list('gastos',flat=True).get(pk=i))
 seg=[]
 imp=[]
 if meses>0 and meses<=12:
                for i in range(1,11):
                   imp.append(Banco.objects.values_list('im_1',flat=True).get(pk=i))
                if seguro=="on":
                 for i in range(1,11):
                   seg.append(Banco.objects.values_list('seguro_1',flat=True).get(pk=i))
                banco=Banco.objects.filter().order_by('im_1')
 elif meses>=13 and meses<=23:
                for i in range(1,11):
                   imp.append(Banco.objects.values_list('im_2',flat=True).get(pk=i))
                if seguro=="on":
                 for i in range(1,11):
                   seg.append(Banco.objects.values_list('seguro_2',flat=True).get(pk=i))
                banco=Banco.objects.filter().order_by('im_2')
 elif meses>=24 and meses<=36:
                for i in range(1,11):
                   imp.append(Banco.objects.values_list('im_3',flat=True).get(pk=i))
                if seguro=="on":
                 for i in range(1,11):
                   seg.append(Banco.objects.values_list('seguro_3',flat=True).get(pk=i))
                banco=Banco.objects.filter().order_by('im_3')
 elif meses>=37 and meses<=48:
                 for i in range(1,11):
                   imp.append(Banco.objects.values_list('im_4',flat=True).get(pk=i))
                 if seguro=="on":
                  for i in range(1,11):
                   seg.append(Banco.objects.values_list('seguro_4',flat=True).get(pk=i))
                 banco=Banco.objects.filter().order_by('im_4')
 elif meses<0 or meses>48:
                imp=-1

 avedul=Banco.compra(float(meses),float(seg[1]),float(gastos[1]),float(imp[1]),monto)
 return render(request, 'creditos/index2.html',{'banco':banco,'seg':seg,'imp':imp,'avedul':avedul})

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
 seg=0
 if meses>0 and meses<=12:
                imp=Banco.objects.values('im_1')
                if seguro=="on":
                   seg=Banco.objects.values('seguro_1')
 elif meses>=13 and meses<=23:
                imp=Banco.objects.values('im_2')
                if seguro=="on":
                   seg=Banco.objects.values('seguro_2')
 elif meses>=24 and meses<=36:
                imp=Banco.objects.values('im_3')
                if seguro=="on":
                   seg=Banco.objects.values('seguro_3')
 elif meses>=37 and meses<=48:
                imp=Banco.objects.values('im_4')
                if seguro=="on":
                   seg=Banco.objects.values('seguro_4')
 elif meses<0 or meses>48:
                imp=-1
#sacar impuesto, seguro, y hacer calculos
 banco=Banco.objects.filter().order_by('cae')
 return render(request, 'creditos/index2.html',{'banco':banco,'seguro':seguro,'seg':seg,'imp':imp})

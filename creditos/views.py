from django.shortcuts import render
from .models import Banco
def post_list(request):
 banco=Banco.objects.filter().order_by('cae')
 return render(request, 'creditos/index.html', {'banco':banco})


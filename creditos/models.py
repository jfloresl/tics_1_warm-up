from django.db import models
from .forms import Regform
class Banco(models.Model):
       cae =models.DecimalField(max_digits=4,decimal_places=2)
       im_1=models.DecimalField(max_digits=4,decimal_places=2)
       im_2=models.DecimalField(max_digits=4,decimal_places=2)
       im_3=models.DecimalField(max_digits=4,decimal_places=2)
       im_4=models.DecimalField(max_digits=4,decimal_places=2)
       seguro_1 =models.IntegerField()
       seguro_2 =models.IntegerField()
       seguro_3 =models.IntegerField()
       seguro_4 =models.IntegerField()
       gastos =models.IntegerField()
       nombre = models.CharField(max_length=200)


       def segu(a):
           return 666

       def compra(meses,seg,gastos,imp,monto):
           return (((monto*((1+(imp/100))**meses)*(imp/100)) / (((1+(imp/100))**meses)-1)) +(seg/meses)+(gastos/meses))*meses

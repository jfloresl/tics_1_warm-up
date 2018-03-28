from django.db import models

class Banco(models.Model):
       cae =models.DecimalField(max_digits=4,decimal_places=2)
       im_1=models.DecimalField(max_digits=4,decimal_places=2)
       im_2=models.DecimalField(max_digits=4,decimal_places=2)
       im_3=models.DecimalField(max_digits=4,decimal_places=2)
       im_4=models.DecimalField(max_digits=4,decimal_places=2)
       seguro =models.IntegerField()
       gastos =models.IntegerField()
       nombre = models.CharField(max_length=200)


       def name(self):
           return self.nombre
       def seg(self):
           return self.seguro
       def gas(self):
           return self.gastos
class Calculator(models.Model):
    monto = models.IntegerField()
    meses = models.IntegerField()

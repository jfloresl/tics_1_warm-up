from django.db import models

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


       def name(self):
           return self.nombre
       def seg(self):
           return 666
           #return self.seguro_1+self.gastos
       def gas(self):
           return self.gastos
       def cuota(self):
           return

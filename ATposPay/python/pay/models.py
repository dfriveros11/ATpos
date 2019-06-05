from django.db import models

# Create your models here.
class Pay(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    value = models.DecimalField(max_digits=20, decimal_places=2)
    buyerid = models.IntegerField()
    methodid = models.IntegerField()
    class Meta:
        db_table = "pay"
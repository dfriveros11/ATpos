from django.db import models

# Create your models here.
class Method(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    class Meta:
        db_table = "method"
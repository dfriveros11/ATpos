from django.db import models

# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    class Meta:
        db_table = "buyer"
    def __str__(self):
        return '%s %s' % (self.name, self.email)
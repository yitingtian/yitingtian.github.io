from django.db import models

# Create your models here.
class register(models.Model):
    Pnumber = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    birthday = models.DateField()
    sex = models.CharField(max_length=10)
    reIdentity = models.CharField(max_length=200)
    Identity = models.CharField(max_length=200)
    tel = models.CharField(max_length=10)
    address = models.CharField(max_length=200)

    class Meta:
        db_table='register'

from django.db import models

# Create your models here.

class register(models.Model):
    name = models.CharField(max_length=50)
    Idnumber = models.CharField(max_length=15)
    birthday = models.DateField()
    sex = models.CharField(max_length=10)
    Identity = models.CharField(max_length=200)
    tel = models.CharField(max_length=10)
    address = models.CharField(max_length=200)

    class Meta:
        db_table='register'


class Getnumber(models.Model):
    name = models.CharField(max_length=50)
    Idnumber = models.CharField(max_length=15)
    birthday = models.DateField()
    sex = models.CharField(max_length=10)
    reIdentity = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
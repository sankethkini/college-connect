from django.db import models
from django.utils.timezone import now

class Teacher(models.Model):
    tid=models.CharField(primary_key=True,max_length=10)
    tname=models.CharField(max_length=20)
    contact=models.BigIntegerField()
    email=models.EmailField(default=None)
    tdept=models.CharField(max_length=20)
    field_of_specialization=models.CharField(max_length=20)
    password=models.CharField(max_length=20,default="connect123")
    def __str__(self):
        return self.tname
from django.db import models
from django.utils.timezone import now
from .Research import Research
class Student(models.Model):
    usn=models.CharField(primary_key=True,max_length=10)
    sname=models.CharField(max_length=15)
    contact=models.BigIntegerField()
    email=models.EmailField(default=None)
    field_of_interest=models.CharField(max_length=20)
    sem=models.IntegerField()
    sdept=models.CharField(max_length=20)
    password=models.CharField(max_length=20,default="connect123")
    rid=models.ForeignKey(to=Research,on_delete=models.CASCADE,default=None, blank=True, null=True)

    def __str__(self):
        return self.sname
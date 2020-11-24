from django.db import models
from django.utils.timezone import now

class Project(models.Model):
    pid=models.AutoField(primary_key=True)
    pname=models.CharField(max_length=20)
    time=models.DurationField()
    starttime=models.DateTimeField(default=now)
    projshortdesc=models.CharField(max_length=50,default=None)
    pfield=models.CharField(max_length=20)
    branch_restriction=models.BooleanField(default=False)
    number_of_people=models.IntegerField()
    people_requested=None
    def __str__(self):
        return self.pname


from django.db import models
from django.utils.timezone import now

class Research(models.Model):
    rid=models.AutoField(primary_key=True)
    rname=models.CharField(max_length=20)
    rfield=models.CharField(max_length=20)
    rnumber_of_people=models.IntegerField()
    duration=models.DurationField()
    rescshortdesc=models.CharField(max_length=50,default=None)
    research_start_time=models.DateTimeField()
    dept_restriction=models.BooleanField()
    people_requested=None
    

    def __str__(self):
        return self.rname

from django.db import models
from django.utils.timezone import now
# Create your models here.

class Project(models.Model):
    pid=models.AutoField(primary_key=True)
    pname=models.TextField()
    time=models.DurationField()
    starttime=models.DateTimeField(default=now)
    pfield=models.CharField(max_length=20)
    branch_restriction=models.BooleanField(default=False)
    number_of_people=models.IntegerField()

    def __str__(self):
        return self.pname

class Research(models.Model):
    rid=models.AutoField(primary_key=True)
    rname=models.TextField()
    rfield=models.CharField(max_length=20)
    rnumber_of_people=models.IntegerField()
    duration=models.DurationField()
    research_start_time=models.DateTimeField()
    dept_restriction=models.BooleanField()

    def __str__(self):
        return self.rname

class Student(models.Model):
    usn=models.CharField(primary_key=True,max_length=10)
    sname=models.CharField(max_length=15)
    contact=models.BigIntegerField()
    field_of_interest=models.CharField(max_length=20)
    sem=models.IntegerField()
    sdept=models.CharField(max_length=20)
    rid=models.ForeignKey(to=Research,on_delete=models.CASCADE,default=None, blank=True, null=True)

    def __str__(self):
        return self.sname

class Teacher(models.Model):
    tid=models.CharField(primary_key=True,max_length=10)
    tname=models.CharField(max_length=20)
    contact=models.BigIntegerField()
    tdept=models.CharField(max_length=20)
    field_of_specialization=models.CharField(max_length=20)

    def __str__(self):
        return self.tname

class Project_Teacher(models.Model):
    class Meta:
        unique_together = ('tid','pid')
    tid=models.ForeignKey(to=Teacher,on_delete=models.CASCADE)
    pid=models.ForeignKey(to=Project,on_delete=models.CASCADE)
 
    def __str__(self):
        return "tid:{} pid:{}".format(self.tid.tid,self,pid.pid)


class Project_Student(models.Model):
    class Meta:
        unique_together = ('pid','usn')
    pid=models.ForeignKey(to=Project,on_delete=models.CASCADE)
    usn=models.ForeignKey(to=Student,on_delete=models.CASCADE)

    def __str__(self):
        return "project id:{} usn:{}".format(self.pid.pid,self.usn.usn)

class Research_Teacher(models.Model):
    class Meta:
        unique_together = ('rid','tid')
    rid=models.ForeignKey(to=Research,on_delete=models.CASCADE)
    tid=models.ForeignKey(to=Teacher,on_delete=models.CASCADE)
    
    def __str__(self):
        return "research id:{} tid:{}".format(self.rid.rid,self.tid.tid)
    
from django.db import models

# Create your models here.
class taskstatus(models.Model):
    status = models.CharField(max_length=100)
    def  __str__(self):
        return self.status

class task(models.Model):
    taskname = models.CharField(max_length=100)
    taskdescription = models.CharField(max_length=1000)
    taskduedate = models.DateField()
    taskstatus = models.ForeignKey(taskstatus, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.taskname
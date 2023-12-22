from django.db import models

# Create your models here.

class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100,unique=True)
    loc=models.CharField(max_length=100)

    def __str__(self):
        return str(self.deptno)
    

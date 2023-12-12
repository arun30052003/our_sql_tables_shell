from django.db import models

# Create your models here.

class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100,unique=True)
    loc=models.CharField(max_length=100)

    def __str__(self):
        return str(self.deptno)
    
class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    MGR=models.CharField(max_length=100)
    Hiredate=models.DateField(max_length=100)
    sal=models.IntegerField()
    comm=models.IntegerField(default=0)
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.ename

from django.shortcuts import render

# Create your views here.
from app.models import *

def dept(request):
    QLTO=Dept.objects.all()
    d={'Dept':QLTO}
    return render(request,'dept.html',d)

def emp(request):
    QLTO=Emp.objects.all()
    d={'Emp':QLTO}
    return render(request,'emp.html',d)

def insert_dept(request):
    dno=input('Enter deptno')
    dna=input('Enter dname')
    l=input('Enter loc')

    NDO=Dept.objects.get_or_create(deptno=dno,dname=dna,loc=l)[0]
    NDO.save()

    QLTO=Dept.objects.all()
    d={'Dept':QLTO}
    return render(request,'dept.html',d)

def insert_emp(request):
    dno=input('Enter deptno')
    eno=input('Enter empno')
    ena=input('Enter empna')
    j=input('Enter job')
    MGR=input('Enter MGR')
    em=input('Enter email')
    hd=input('Enter hiredate')
    s=input('Enter sal')
    c=input('Enter comm')

    NDO=Dept.objects.get(deptno=dno)
    NEO=Emp.objects.get_or_create(deptno=NDO,empno=eno,ename=ena,job=j,MGR=MGR,email=em,Hiredate=hd,sal=s,comm=c)[0]
    NEO.save()

    QLTO=Emp.objects.all()
    d={'Emp':QLTO}
    return render(request,'emp.html',d)
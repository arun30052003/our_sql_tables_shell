from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length

def dept(request):
    QLTO=Dept.objects.all()
    QLTO=Dept.objects.all().order_by(Length('dname').desc())
    QLTO=Dept.objects.filter(deptno__in=('1','4'))
    
    d={'Dept':QLTO}
    return render(request,'dept.html',d)

def emp(request):
    QLTO=Emp.objects.all()
    QLTO=Emp.objects.all().order_by('ename')
    QLTO=Emp.objects.all().order_by('-ename')
    QLTO=Emp.objects.all().order_by(Length('ename'))
    QLTO=Emp.objects.all().order_by(Length('ename').desc())
    QLTO=Emp.objects.all().order_by('empno')[::]
    QLTO=Emp.objects.exclude(ename='sivangi')
    QLTO=Emp.objects.filter(Hiredate__month=5)
    QLTO=Emp.objects.filter(Hiredate__year=2023)
    QLTO=Emp.objects.filter(Hiredate__day=10)
    QLTO=Emp.objects.filter(sal__lte=50000)
    QLTO=Emp.objects.filter(deptno__in=('2','3'))
    QLTO=Emp.objects.filter(pk__in=(11,))
    QLTO=Emp.objects.filter(pk__in=(11,20))
    QLTO=Emp.objects.filter(pk__in=('11','20'))
    QLTO=Emp.objects.filter(ename__in=('Anjali','Sumithra'))
    QLTO=Emp.objects.filter(sal__lt=50000)


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
from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
def dept(request):
    QLTO=Dept.objects.all()
    QLTO=Dept.objects.all().order_by(Length('dname').desc())
    QLTO=Dept.objects.filter(deptno__in=('1','4'))
    QLTO=Dept.objects.all()
    
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
    QLTO=Emp.objects.filter(sal__lt=50000)
    QLTO=Emp.objects.filter(sal__lte=50000)
    QLTO=Emp.objects.filter(sal__gt=50000)
    QLTO=Emp.objects.filter(sal__gte=50000)
    QLTO=Emp.objects.filter(deptno__in=('2','3'))
    QLTO=Emp.objects.filter(pk__in=(11,))
    QLTO=Emp.objects.filter(pk__in=(11,20))
    QLTO=Emp.objects.filter(pk__in=('11','20'))
    QLTO=Emp.objects.filter(ename__in=('Anjali',))
    QLTO=Emp.objects.filter(ename__in=('Anjali','Sumithra'))
    QLTO=Emp.objects.filter(ename__in=['Anjali'])
    QLTO=Emp.objects.filter(ename__in=['Anjali','Sumithra'])
    QLTO=Emp.objects.filter(ename__contains='A',sal__gt=50000)
    QLTO=Emp.objects.filter(Q(ename__startswith='A') & Q(sal__lt=50000))
    QLTO=Emp.objects.filter(Q(ename__contains='j') | Q(MGR__gt=200))
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


def update_dept(request):
    Dept.objects.filter(deptno=1).update(dname='coding')
    Dept.objects.filter(dname='Coder').update(loc='ABC')
    Dept.objects.filter(loc='ABC').update(dname='coder')
    Dept.objects.filter(dname='Builder').update(loc='TamilNadu')
    Dept.objects.update_or_create(deptno=7,defaults={'dname':'WEB','loc':'Delhi'})
    Dept.objects.update_or_create(deptno=3,defaults={'dname':'Builders','loc':'Kochi'})

    Dept.objects.filter(pk=9).update(deptno=15)
    QLTO=Dept.objects.all()
    d={'Dept':QLTO}
    return render(request,'dept.html',d)


def update_emp(request):
    Emp.objects.filter(empno=1).update(deptno=1)
    Emp.objects.filter(ename='Arun').update(deptno=3)
    Emp.objects.filter(ename='Arun').update(empno=2)
    Emp.objects.filter(job='HR').update(empno=3)
    Emp.objects.update_or_create(empno=23,defaults={'ename':'Sivangi','MGR':'456'})
    Emp.objects.update_or_create(deptno=1,defaults={'empno':'13','ename':'Brindha','job':'Trainer','MGR':'1000','email':'santhosh@gmail.com','Hiredate':'2022-02-10','sal':'80000','comm':'500'})
    NDO=Dept.objects.get(deptno=4)
    Emp.objects.update_or_create(deptno=NDO,defaults={'empno':'24','ename':'Ramya','job':'Trainer','MGR':'1000','email':'santhosh@gmail.com','Hiredate':'2022-02-10','sal':'80000','comm':'500'})
    Emp.objects.filter(ename='Sivangi').update(empno='147')

    QLTO=Emp.objects.all()
    d={'Emp':QLTO}
    return render(request,'emp.html',d)


def delete_dept(request):
    #Dept.objects.filter(deptno=1).delete()
    Dept.objects.filter(dname='QWE').delete()
    Dept.objects.filter(loc='Mumbai').delete()
    Dept.objects.filter(pk=3).delete()
    Dept.objects.all().delete()

    QLTO=Dept.objects.all()
    d={'Dept':QLTO}
    return render(request,'dept.html',d)


def delete_emp(request):
    #Emp.objects.filter(deptno=1).delete()
    Emp.objects.filter(empno=1).delete()
    Emp.objects.filter(pk=22).delete()
    Emp.objects.filter(ename='Arun').delete()
    Emp.objects.all().delete()

    QLTO=Emp.objects.all()
    d={'Emp':QLTO}
    return render(request,'emp.html',d)





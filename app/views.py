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



def insert_dept(request):
    dno=input('Enter deptno')
    dna=input('Enter dname')
    l=input('Enter loc')

    NDO=Dept.objects.get_or_create(deptno=dno,dname=dna,loc=l)[0]
    NDO.save()

    QLTO=Dept.objects.all()
    d={'Dept':QLTO}
    return render(request,'dept.html',d)



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


def delete_dept(request):
    #Dept.objects.filter(deptno=1).delete()
    Dept.objects.filter(dname='QWE').delete()
    Dept.objects.filter(loc='Mumbai').delete()
    Dept.objects.filter(pk=3).delete()
    Dept.objects.all().delete()

    QLTO=Dept.objects.all()
    d={'Dept':QLTO}
    return render(request,'dept.html',d)





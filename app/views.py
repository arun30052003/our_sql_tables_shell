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
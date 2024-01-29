from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import *
from django.db.models.functions import Length

def topic(request):
    QLTO=Topic.objects.all()
    d={'Topic':QLTO}
    return render(request,'Topic.html',d)

def webpage(request):
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.all().order_by('name')
    QLWO=Webpage.objects.all().order_by('-name')
    QLWO=Webpage.objects.all().order_by(Length('name'))
    QLWO=Webpage.objects.all().order_by(Length('name').desc())
    QLWO=Webpage.objects.filter(topic_name='Basball').order_by(Length('name'))
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.filter(topic_name='Kabaddi',name__startswith='n')
    QLWO=Webpage.objects.all()
    webpage.objects.filter(topic_name='cricket').update(name='giri')

    d={'webpage':QLWO}
    return render(request,'webpage.html',d)

def acessrecord(request):
    QLAO=AccessRecord.objects.all()
    d={'acessrecord':QLAO}
    return render(request,'acessrecord.html',d)


def insert_topic(request):
    tn=input('enter a tp')
    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()
    return HttpResponse('Topic is inserted-------')

def insert_webpage(request):
    tn=input('enter a tp')
    n=input('enter name')
    u=input('enter url')
    e=input('enter email')
    TO=Topic.objects.get(topic_name=tn)
    WPO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,Email=e)[0]
    WPO.save()
    return render(request,'Webpage.html')

def insert_acessrecord(request):
    pk=int(input())
    a=input()
    d=input()
    WO=Webpage.objects.get(pk=pk)
    ACO=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)[0]
    ACO.save()
    return render(request,'acessrecord.html')







def update_webpage(request):
    Webpage.objects.filter(topic_name='cricket').update(name='Allukuru Giri')



    QLWO=Webpage.objects.all()
    d={'webpage':QLWO}
    return render(request,'webpage.html',d)


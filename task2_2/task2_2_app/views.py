from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.response import TemplateResponse
from task2_2_app.models import *
from dataclasses import dataclass
# Create your views here.




def index(request):
    Races = BusRaces.objects.all()
    Bus = Buses.objects.all()
    context = {
        "BusRaces": Races,
        "Buses": Bus,
    }
    return TemplateResponse(request, "index.html", context)


def removingRaces(request, num):
    BusRaces.objects.get(id=num).delete()
    return redirect('/')

def removingBuses(request, num):
    Buses.objects.get(id=num).delete()
    return redirect('/')


def form(request, num=0):
    isBusForm = request.GET.get("bus")
    Races = makeRaces(isBusForm)
    context = {
        "BusRaces" : Races,
        "isBusForm": isBusForm,
        }
    return TemplateResponse(request, "form.html", context)


def addRace(request):
    date = request.POST.get("date")
    time = request.POST.get("time")
    race = request.POST.get("race")
    BusRaces.objects.create(date=date, time=time, fromTo=race)
    return redirect('/')

def addBus(request, num=0):
    number = request.POST.get("number")
    mileAge = request.POST.get("mileAge")
    race = request.POST.get("race")
    foreignKey = BusRaces.objects.get(id=race)
    Buses.objects.create(number=number, mileAge=mileAge, Busrace=foreignKey)
    return redirect('/')

def editing(request, id):
    isBusForm = request.GET.get("bus")
    Races = makeRaces(isBusForm)
    context = {
        "BusRaces": Races,
        "isBusForm": isBusForm,
        "id": id,
    }
    return TemplateResponse(request, "form.html", context)

def editBus(request, id):
    race = request.POST.get("race")
    number = request.POST.get("number")
    mileAge = request.POST.get("mileAge")
    foreignKey = BusRaces.objects.get(id=race)
    Bus = Buses.objects.filter(id=id).update(Busrace=foreignKey, number=number, mileAge=mileAge)
    return redirect('/')

def editRace(request, id): 
    date = request.POST.get("date")
    time = request.POST.get("time")
    fromTo = request.POST.get("race")
    Race = BusRaces.objects.filter(id=id).update(date=date, time=time, fromTo=fromTo)
    return redirect('/')



def makeRaces(isBusForm):
    @dataclass
    class RaceObj():
        def __init__(self, id, fromTo): 
            self.id = id
            self.fromTo = fromTo
            def __str__(self): 
                return self.fromTo
            
    if (isBusForm == "true"):
        Races = [RaceObj(Race.pk, Race.__str__()) for Race in BusRaces.objects.all()]
        
    else:
        Races = [RaceObj(Race[0], Race[1]) for Race in BusRaces.RACES]
    return Races
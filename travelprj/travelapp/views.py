from django.shortcuts import render

from . models import Locations

from . models import Team

def index(request):
    obj=Locations.objects.all()
    obj1=Team.objects.all()
    return render(request,"index.html",{'object':obj,'object1':obj1})

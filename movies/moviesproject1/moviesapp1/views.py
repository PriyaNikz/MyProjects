from django.http import HttpResponse
from . models import movies_dtl
from django.shortcuts import render, redirect
from . forms import MovieForm


def index(request):
    movies=movies_dtl.objects.all()
    context={
        'movies_list': movies
    }
    return render(request,"index.html",context)

def detail(request,movie_id):
    movie=movies_dtl.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movie})

def add_movies(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        year=request.POST.get('year',)
        desc=request.POST.get('desc',)
        pic=request.FILES['pic']
        movie=movies_dtl(name=name,year=year,desc=desc,pic=pic)
        movie.save()
    return render(request,"add.html")

def update(request,movie_id):
    movie=movies_dtl.objects.get(id=movie_id)
    form=MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html", {'form':form,'movie':movie})
def delete(request,movie_id):
    if request.method=='POST':
        movie=movies_dtl.objects.get(id=movie_id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')



from django.http import HttpResponse
from django.shortcuts import render, redirect

from movieapp.forms import MovieForm
from movieapp.models import movie


# Create your views here.
def index(request):
    movie_list = movie.objects.all()
    context ={
        "movie_list" : movie_list
    }
    return render(request,'index.html',context)




def details(request,movie_id):
    mvie = movie.objects.get(id=movie_id)
    return render(request,'details.html',{'movie' : mvie})

def add(request):
    if request.method == 'POST':
        mname = request.POST['mname']
        year = request.POST['year']
        img = request.FILES['img']
        desc = request.POST['desc']
        mov = movie.objects.create(mname=mname,year=year,img=img,desc=desc)
        mov.save()


    return render(request,'add.html')
def movie_edit(request,id):
    mvid = movie.objects.get(id = id)
    form = MovieForm(request.POST or None,request.FILES,instance=mvid)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'update.html',{'mvid':mvid,'form':form})

def delete(request,id):
    if request.method == "POST":
        mv = movie.objects.get(id=id)
        mv.delete()
        return redirect('/')
    return render(request,'delete.html')
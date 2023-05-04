from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import Task
from . forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


class TaskListView(ListView):
    model=Task
    template_name = 'add.html'
    context_object_name = 'task1'

class TaskDetailView(DetailView):
    model=Task
    template_name = 'detail.html'
    context_object_name = 'task1'

class TaskUpdateView(UpdateView):
    model=Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields=('task','priority','date')

    def get_success_url(self):
         return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')

def add(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        task=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        tsk=Task(task=task,priority=priority,date=date)
        tsk.save()
    return render(request,"add.html",{'task1':task1})

def delete(request,taskid):
    task= Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,"delete.html")

def update(request,tid):
    task=Task.objects.get(id=tid)
    form=TodoForm(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'task':task})

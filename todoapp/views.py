from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .Form import *
# Create your views here.


def index(request):
    #get information from the model
    tasks=Task.objects.all()
    #make a copy of the form in this variable to send it to the template
    form=TaskForm()
    #add a new task
    if request.method == 'POST':
        #make data we got it from request in this variable to send it to the template
        form= TaskForm(request.POST)
        if form.is_valid():#if the data is valid add it to the db
            form.save()
        return redirect('/')#go back to our page
    context={'tasks':tasks,'form':form}
    return render(request,'list.html',context)  



#this view for the update functionality
def UpdateTask(request,pk):
    task=Task.objects.get(id=pk)#get the precise task
    form = TaskForm(instance=task)#this is from precising wich task we wanna update
    #make the update
    if request.method == 'POST':
        form=TaskForm(request.POST,instance=task)#this is for updating the same item without creating a new item
        if form.is_valid():
            form.save()
            return redirect('/')#go back to our index page
    context={'form':form}
    return render(request,'update_task.html',context)

def deleteTask(request,pk):
    task=Task.objects.get(id=pk)
    #make the delete
    if request.method == 'POST':
        task.delete()#deleting the task
        return redirect('/')#go back to the main page
    context={'item':task.title}
    return render(request,'delete_task.html',context)
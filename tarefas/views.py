from django.shortcuts import render,redirect, get_object_or_404
from .forms import TarefaForm
from .forms import TarefaModel
from django.http import HttpRequest

def tarefa(request):
    context = {
        "nome" : "Frank Montes",
        "tarefas" : TarefaModel.objects.all()
    }
    return render(request,'tarefas/home.html',context)


def adicionar_tarefa(request):
    if request.method == "POST":
        formulario = TarefaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("tarefas:home") 
    context = {
        "form":TarefaForm
    }
    return render(request,"tarefas/adicionar.html",context)


def remover_tarefa(request:HttpRequest,id):
    tarefa = get_object_or_404(TarefaModel,id=id)
    tarefa.delete()
    return redirect("tarefas:home")

def editar_tarefa(request:HttpRequest,id):
    tarefa = get_object_or_404(TarefaModel, id=id)
    if request.method == "POST":
        formulario = TarefaForm(request.POST, instance=tarefa)
        if formulario.is_valid():
            formulario.save()
            return redirect("tarefas:home")
        
    formulario = TarefaForm(instance=tarefa)
    context = {
        'form':formulario
    }
    return render(request,'tarefas/editar.html',context)
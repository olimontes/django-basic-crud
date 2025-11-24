from django.urls import path
from . import views

app_name = "tarefas"

urlpatterns = [
    path("", views.tarefa,name="home"),
    path("adicionar/",views.adicionar_tarefa,name="adicionar"),
    path("remover/<int:id>",views.remover_tarefa,name="remover"),
    path("editar/<int:id>",views.editar_tarefa,name="editar")
]
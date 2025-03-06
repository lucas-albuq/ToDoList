from django.urls import path
from tarefas import views

urlpatterns = [
    path('<uuid:id>/', views.equipe_detalhes, name='equipe_detalhes'),
]

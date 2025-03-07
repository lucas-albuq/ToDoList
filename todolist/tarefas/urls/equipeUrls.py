from django.urls import path
from tarefas import views

urlpatterns = [
    path('<uuid:id>/', views.EquipeViews.equipe_detalhes, name='equipe_detalhes'),
]

from django.urls import path
from tarefas.views import cadastro, login_view, logout_view, google_login, google_callback

urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('google/login/', google_login, name='google_login'),
    path('google/callback/', google_callback, name='google_callback'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_instrutor, name='cadastrar'),
    path('listar/', views.listar, name='listar'),
    path('cadastro/', views.carregar_cadastro, name='cadastro')

]
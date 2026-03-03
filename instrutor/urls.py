from django.urls import path
from . import views

app_name = 'instrutor'


urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('listar/', views.listar, name='listar'),
    path('cadastro/', views.carregar_cadastro, name='cadastro')
]
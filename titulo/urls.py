from django.urls import path
from titulo import views

app_name = 'titulo'

urlpatterns = [
    path("listar/", views.listar, name="listar"),
    path("cadastro/", views.carregar_titulo, name='cadastro')
]

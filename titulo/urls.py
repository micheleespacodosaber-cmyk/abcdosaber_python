from django.urls import path
from titulo import views

app_name = 'titulo'

urlpatterns = [
    path("lista/", views.listar, name="listar_titulo"),
]

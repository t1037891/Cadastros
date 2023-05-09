from django.urls import path
from CadastroCliente import views

urloatterns = [
    path('', views.index, name='index'),
]
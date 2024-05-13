from django.urls import path #Faz o roteamento das requisições
from galeria.views import index #Importando função index da views.py

#Criando uma lista de endereço e endpoints para a galeria.
#O urlpatterns da galeria tem que ser acessado pelo urls.py da pasta setup

urlpatterns = [
    path('', index)
]
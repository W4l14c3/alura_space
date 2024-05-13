from django.shortcuts import render
from django.http import HttpResponse

#Função que vai responder uma requisição, e enviar uma pagina(Renderizar.)
def index(request):
    return HttpResponse('<h1>Alura Space</h1>')
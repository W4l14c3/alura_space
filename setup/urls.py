from django.contrib import admin
from django.urls import path,include

urlpatterns = [ #Urls padroes.
    path('admin/', admin.site.urls),
    path('',  include('galeria.urls')), #A urls.py da galeria sera chamada quando a requisição for a pagina principal e vai executar seu conteudo.
]

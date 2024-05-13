from django.contrib import admin
from django.urls import path, include
from galeria.views import index # Função index importada de views

urlpatterns = [ #Urls padroes.
    path('admin/', admin.site.urls),
    path('',  index), #A função index será executada quando o endereco principal for requisitado
]

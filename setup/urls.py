from django.contrib import admin
from django.urls import path,include

urlpatterns = [ #Urls padroes.
    path('admin/', admin.site.urls),
    
    #Aqui só direcionamos a responsabilidade para a galeria.
    path('',  include('galeria.urls')), #A urls de galeria faz parte da urls setup.
]

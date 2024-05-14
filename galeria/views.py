from django.shortcuts import render

#Função que vai responder uma requisição, e enviar uma pagina(Renderizar.)
#Vai devolver uma resposta, no caso uma pagina html
#Recebe: '' no parâmetro request, de urls.py e retorna uma pagina html renderizada do TEMPLATES.
def index(request):
    return render(request, 'galeria/index.html')
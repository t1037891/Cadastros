from django.shortcuts import render

# Create your views here.
def index(request):
    meu_nome = 'Camila Souza'
    lista_frutas = ['Laranja', 'Maça', 'Banana']
    context = {
        'nome' : meu_nome,
        'frutas' : ['Laranja', 'Maça', 'Banana']
        }
    return render(request, 'index.html', context)
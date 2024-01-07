
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def hola_mundo(request):
        return HttpResponse("Holaaaaa Maríaaa! :)")

def index(request):
    lenguajes= ['Python','Nodejs', 'PHP']
    return render(request, 'index.html',{
        'mi_variable':'Soy un dato que está en la vista',
         'nombre':'Franulo',
        'languages' : lenguajes, #lista definida anteriormente
        'titulo' : 'inicio(variable)'
    })
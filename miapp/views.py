
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def hola_mundo(request):
        # return HttpResponse("Holaaaaa Maríaaa! :)")
        return redirect('https://google.com')
        # puedo redireccionar con parámetros tb: redirect('autocad', user='fran', pwd='123')
def index(request):
    lenguajes= ['Python','Nodejs', 'PHP']
    return render(request, 'index.html',{
        'mi_variable':'Soy un dato que está en la vista',
         'nombre':'Franulo',
        'languages' : lenguajes, #lista definida anteriormente
        'descripcion' : 'Estudio de arquitectura de Francisco Jerez García',
        'titulo' : 'Home'
    })

def autocad(request, user='', pwd=''):  
    # las comillas para que seas opcionales
    return HttpResponse(f"{user}, {pwd}")

def listaObras(request):  
    # las comillas para que seas opcionales
    return render(request, 'listaObras.html', {
        'titulo' : 'Obras'
    })

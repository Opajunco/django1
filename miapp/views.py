
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article, Category, Pais, Ciudad

# Create your views here.


def hola_mundo(request):
    # return HttpResponse("Holaaaaa Maríaaa! :)")
    return redirect('https://google.com')
    # puedo redireccionar con parámetros tb: redirect('autocad', user='fran', pwd='123')


def index(request):
    lenguajes = ['Python', 'Nodejs', 'PHP']
    return render(request, 'index.html', {
        'rec': request,
        'mi_variable': 'Soy un dato que está en la vista',
        'nombre': 'Franulo',
        'languages': lenguajes,  # lista definida anteriormente
        'descripcion': 'Estudio de arquitectura de Francisco Jerez García',
        'titulo': 'Home'
    })


def autocad(request, user='', pwd=''):
    # las comillas para que seas opcionales
    return HttpResponse(f"{user}, {pwd}")





def crear_articulo(request, title, content, public):
    articulo = Article(
        title=title,
        content=content,
        public=public,
    )
    articulo.save()
    return HttpResponse(f"Articulo creado: {articulo.title}")


def articulo(request, pk):

    try:
        articulo = Article.objects.get(pk=pk)
        response = f"Articulo: {articulo.title}"
    except:
        response = "Articulo no encontrado"

    return HttpResponse(response)


def articulos(request):

    articulos = Article.objects.all()

    return render(request, 'articulos.html', {
        'articulos': articulos,
        'titulo': "Artículos",
    })


def get_paises(request):
    paises = list(Pais.objects.values())

    if len(paises) > 0:
        data = {'message': 'Success', 'paises': paises}
    else:
        data = {'message': 'not found'}
    return JsonResponse(data)

def indexpaises(request):
    return render(request,'indexpaises.html')

def get_ciudades(request, pais_id):
    ciudades=list(Ciudad.objects.filter(pais_id=pais_id).values())
    
    if len(ciudades) > 0:
        data = {'message': 'Success', 'ciudades': ciudades}
    else:
        data = {'message': 'not found'}
    return JsonResponse(data)
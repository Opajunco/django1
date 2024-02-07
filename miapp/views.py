
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article, Category, Pais, Ciudad
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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
    # return HttpResponse(f"{user}, {pwd}")  
          
    user = authenticate(request, username=user, password=pwd)
        
    if user is not None:
        return HttpResponse("true") 
    else:
        messages.warning(request, 'No te has identificado correctamente')
        return HttpResponse("false") 
     
    # return render(request, 'users/login.html', {'titulo':'Login'})






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


def register(request):
    register_form = RegisterForm()
    
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        
    if register_form.is_valid():
        register_form.save()
        messages.success(request,"Te has registrado correctamente")
        return redirect('index')
    
    
    
    
    return render(request,'users/register.html', {
        'titulo':'Registro',
        'register_form':register_form
        })
    
    
def login_page(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.warning(request, 'No te has identificado correctamente')
    
    
    return render(request, 'users/login.html', {'titulo':'Login'})

def logout_user(request):
    logout(request)
    return redirect('login')



@login_required(login_url='login')
def flexbox(request): 
    partidas =['enfoscado de cemento', 'alicatado en baño', 'falso techo', 'cocina', 'picado de pared exterior', 'pintado de rejas', 'asdñlfkjalñkdkf', 'añlsdkfjffladf','aslfdjkldaf']   
    return render(request, 'flexbox.html', {
        'titulo':'flexbox',
        'partidas': partidas 
        })

@login_required(login_url='login')
def flexbox2(request):    
    return render(request, 'flexbox2.html', {'titulo':'flexbox2' })


def tasascee(request):
    lenguajes = ['Python', 'Nodejs', 'PHP']
    return render(request, 'tasascee.html')
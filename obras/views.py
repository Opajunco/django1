from django.shortcuts import render

# Create your views here.

def listaObras(request):
    bloque1 = [0,1,2,3,4]
    bloque2 = [5,6,7,8]
    # las comillas para que seas opcionales
    return render(request, 'listaObras.html', {
        'titulo': 'Obras', 
        'bloque1' : bloque1, 
        'bloque2' : bloque2, 
    })
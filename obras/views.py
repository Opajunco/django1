from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from obras.models import Obra


# Create your views here.

def listaObras(request):
    obras = list()
    bloque1 = [0, 1, 2, 3, 4]
    bloque2 = [5, 6, 7, 8]
    # las comillas para que seas opcionales
    return render(request, 'listaObras.html', {
        'titulo': 'Obras',
        'bloque1': bloque1,
        'bloque2': bloque2,
    })


def get_obras(request):
    obras = list(Obra.objects.order_by('ended').values())

    if len(obras) > 0:
        data = {'message': 'Success', 'obras': obras}
    else:
        data = {'message': 'not found'}
    return JsonResponse(data)

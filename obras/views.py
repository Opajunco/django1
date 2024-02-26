from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from obras.models import Obra, PartGen, PartGenDB, PartResult
from miapp.models import Article, Category, Pais, Ciudad
# from user.models import Employee, Org
# from django.contrib.auth.models import AbstractUser, User
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def listaObras(request):
    obras = list()

    # las comillas para que seas opcionales
    return render(request, 'listaObras.html', {
        'titulo': 'Obras',
    })


def get_obras(request):
    current_user = request.user
    # print ("el usuarioooooooooooooooo")
    # print (current_user.id)
    
    if (current_user.id):
        print (current_user.id)
    else:
        print ("no hay usuarioooooooo")
        
    obras = list(Obra.objects.filter(org= current_user.employee.org.id ).order_by('ended').values())

    if len(obras) > 0:
        data = {'message': 'Success', 'obras': obras}
    else:
        data = {'message': 'not found'}
    return JsonResponse(data)



#  ahora esta funcion devuelve las obras en json, pero deberá devolver las partidas
def get_partidas_json(request,idObra, text=''):
    current_user = request.user
    # a = PartGen.objects.filter(id_partresult__pk=1) 
    partis = list(PartResult.objects.filter(obra__pk=idObra).prefetch_related('id_obra').values())
    parti2 = list(PartResult.objects.filter(obra__pk=1).values())
    parti3 = list(PartResult.objects.filter(obra__pk=1).values('obra__titulo', 'title'))
    parti4 = list(PartGen.objects.filter(partresult__obra=idObra).values('partresult__title','partresult__comments', 'cantidad', 'partgendb__descripcion', 'partgendb__unit__name', 'partgendb__capitulo__name' ))

    if (text==''): obras = parti4
    else: obras = list(Obra.objects.filter(concepto__icontains = text ).values())
    

    if len(obras) > 0:
        data = {'message': 'Success', 'obras': obras, }
    else:
        data = {'message': 'not found'}
    return JsonResponse(data)

@login_required(login_url='login')
def partidas(request, idObra):

    return render(request, 'partidas.html', {        
        'titulo': 'Partidas',
        'idObra':idObra ,
    })
    
def get_partidas_html(request,idObra, text=''):
    current_user = request.user
    parti4 = list(PartGen.objects.filter(partresult__obra=idObra).values('id', 'partresult__id', 'partresult__title','partresult__comments', 'cantidad', 'partgendb__descripcion','partgendb__precio_unit', 'partgendb__unit__ab', 'partgendb__capitulo__name' ))
    if (text==''): partidas = parti4
    else: partidas = list(Obra.objects.filter(concepto__icontains = text ).values()) 
    # la parte del else está mal 
    
    # data = {'partidas': partidas}
    # return JsonResponse(data)
    
    return render(request, 'get-partidas.html', {
    'titulo': 'partidas', 
    'partidas': partidas,
    'indice': '0' ,
    })
    
def editfieldspartis(request, editcode, id, content):
    
    if editcode=='update-comment':
        parti = PartResult.objects.get(pk=id)
        parti.comments = content
        parti.save(update_fields=['comments'])
        data = {'message': 'comments updated', 'comments': parti.comments}
        return JsonResponse(data)
    
    elif editcode=='update-med':
        partigen = PartGen.objects.get(pk=id)
        partigen.cantidad = content
        partigen.save(update_fields=['cantidad'])
        partigen = PartGen.objects.get(pk=id) 
        # //esto es para refrescar la información guardada en la base de datos
        # para evitar los numeros con muchos decimales, etc
        print(partigen.cantidad)
        data = {'message': 'comments updated', 'cantidad': partigen.cantidad}
        return JsonResponse(data)
    
    if editcode=='update-title':
        parti = PartResult.objects.get(pk=id)
        parti.title = content
        parti.save(update_fields=['title'])
        data = {'message': 'title updated', 'comments': parti.title}
        return JsonResponse(data)

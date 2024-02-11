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
    partidas =['enfoscado de cemento dfsgd sdfg sdg sdfgsegserg rg sdgshsrhtsrth rth rthfhrth rg rhetherthwrgshdfhdh rthrth sfhddfhdfghdrthrtdhdghdf '
               , 'alicatado en baño hdfghdhssldkgj sfgjsddlkg slñkfgjsñlkfgj sñdlkgjsñijgñdfjgñlksdj gñlksj dfñglkjs lkgj sñldkg sdlfg'
               , 'falso techo dsgls dflñj dfñglsjfñlgjsñdlfgjksñlkfjgñlsdfjñglkjsdfñlkgjdfkjgñlksdjfgñlkjsdlfkgjsd gsd fkjdfglksjd gñlsjd ñfgkjsdgj sdgj lñskfjgñlskdjf gsdjfskf', 'cocina'
               , 'picado de pared exterior'
               , 'pintado de rejas', 'asdñlfkjalñkdkf', 'añlsdkfjffladf','aslfdjkldaf']   

    return render(request, 'partidas.html', {
        'partidas': partidas,
        'titulo': 'Partidas',
    })
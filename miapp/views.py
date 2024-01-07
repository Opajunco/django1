
from django.shortcuts import render, HttpResponse

# Create your views here.


def hola_mundo(request):
        return HttpResponse("Holaaaaa Maríaaa! :)")
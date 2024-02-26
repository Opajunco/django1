from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaObras, name='listaObras'),
    path('get-obras/', views.get_obras, name='get_obras'),
    path('get-partidas-json/<int:idObra>/', views.get_partidas_json, name='get_partidas_json'),
    path('get-partidas-json/<int:idObra>/<str:text>/', views.get_partidas_json, name='get_partidas_json_filtered'),
    path('partidas/<int:idObra>/', views.partidas, name='partidas'),
    path('getpartis/<int:idObra>/', views.get_partidas_html, name='get_partidas'),
    path('editfieldspartis/<str:editcode>/<int:id>/<str:content>/', views.editfieldspartis, name='editfieldspartis'),
    ]



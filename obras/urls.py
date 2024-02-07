from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaObras, name='listaObras'),
    path('get-obras/', views.get_obras, name='get_obras'),
    path('get-partidas-json/<int:idObra>/', views.get_partidas_json, name='get_partidas_json'),
    path('get-partidas-json/<int:idObra>/<str:text>/', views.get_partidas_json, name='get_partidas_json_filtered'),
    ]



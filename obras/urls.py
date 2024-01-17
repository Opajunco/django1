from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaObras, name='listaObras'),
    path('get-obras/', views.get_obras, name='get_obras'),   
]



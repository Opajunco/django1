from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexpaises, name='indexpaises'),
    path('paises/', views.get_paises, name='get_paises'),
    path('ciudades/<int:pais_id>', views.get_ciudades, name='get_ciudades'),
    path('ciudades/<int:pais_id>', views.get_ciudades, name='get_ciudades'),
    
    path('flexbox/', views.flexbox, name='flexbox'), 
    path('flexbox2/', views.flexbox2, name='flexbox2'),
    path('tasascee/', views.tasascee, name='tasascee')
]  


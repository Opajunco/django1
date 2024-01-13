from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexpaises, name='indexpaises'),
    path('paises/', views.get_paises, name='get_paises'),
    path('ciudades/<int:pais_id>', views.get_ciudades, name='get_ciudades')
]

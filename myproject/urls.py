"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#mis vistas
from miapp import views as miappViews
from obras import views as obrasViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', miappViews.index, name='index'), #como he importado views anteriormente no tengo que poner miapp
    path('autocad/<str:user>/<str:pwd>', miappViews.autocad, name='autocad'),
    path('google',miappViews.hola_mundo, name='google'),
    path('crear-articulo/<str:title>/<str:content>/<str:public>', miappViews.crear_articulo, name='crear_articulo'),
    path('articulo/<int:pk>', miappViews.articulo, name='articulo'),
    path('articulos/', miappViews.articulos, name='articulos'),
    path('flexbox/', miappViews.flexbox, name='flexbox'),
    path('miapp/', include('miapp.urls')),
    path('obras/', include('obras.urls')),    
]

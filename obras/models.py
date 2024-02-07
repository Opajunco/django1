from django.db import models
from user.models import Org
from django.contrib.auth.models import AbstractUser, User

# Create your models here.


class Obra(models.Model):
    titulo = models.CharField(max_length=100)
    concepto = models.CharField(max_length=300)
    comentarios = models.TextField()
    diario = models.TextField()      
    porcGg = models.DecimalField(max_digits= 6, decimal_places=4)
    porcBi = models.DecimalField(max_digits= 6, decimal_places=4)
    gastosFijos = models.DecimalField(max_digits= 10, decimal_places=4)    
    image = models.ImageField(default='null')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ended = models.BooleanField(default = False)
    org = models.ForeignKey(Org, on_delete=models.CASCADE,default = 1)
    
    # pais = models.ForeignKey(
    # Pais, null=False, blank=False, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return "{}".format(self.titulo)
        # return super().__str__()
  
class Unit(models.Model):
    name = models.CharField(max_length=20)
    ab = models.CharField(max_length=5)
    order = models.IntegerField()
    
    def __str__(self) -> str:
        return "{}".format(self.name)
  
    
class Capitulo(models.Model):
    name = models.CharField(max_length=50)
    order = models.IntegerField()
    def __str__(self) -> str:
        return "{}".format(self.name)  
  

      
class PartGenDB(models.Model):
    org = models.ForeignKey(Org, on_delete=models.CASCADE)   
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    capitulo = models.ForeignKey(Capitulo, on_delete=models.CASCADE)    
    precio_unit = models.DecimalField(max_digits= 12, decimal_places=4)
    descripcion = models.TextField(max_length=600)
    comentarios = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return "{}".format(self.descripcion)
    
 
 
 
class Zona(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    order = models.IntegerField()
    def __str__(self) -> str:
        return "{}".format(self.name)
    
class Fase(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    order = models.IntegerField()
    def __str__(self) -> str:
        return "{}".format(self.name) 
 
 
class PartResult(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    # id_previa = models.ForeignKey('self', on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    comments = models.TextField(blank=True) 
    
    checklater = models.BooleanField(default=False)
    checkdel = models.BooleanField(default=False)
    checkended = models.BooleanField(default=False)
        
    precio_unit_mod = models.DecimalField(max_digits= 12, decimal_places=4)
   
    def __str__(self) -> str:
        return "{}".format(self.title)   
 
    
class PartGen(models.Model):
    partgendb = models.ForeignKey(PartGenDB, on_delete=models.CASCADE)
    partresult = models.ForeignKey(PartResult, on_delete=models.CASCADE)
    precio_unit_mod = models.DecimalField(max_digits= 12, decimal_places=4)
    cantidad = models.DecimalField(max_digits= 12, decimal_places=4)
    
    
    

    

    
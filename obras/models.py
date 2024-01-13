from django.db import models

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
    
    # pais = models.ForeignKey(
    # Pais, null=False, blank=False, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return "{}".format(self.titulo)
        # return super().__str__()
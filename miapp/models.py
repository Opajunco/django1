from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(default='null')
    public = models.BooleanField(default='False')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    created_at = models.DateField()


class Pais(models.Model):
    nombre = models.CharField(max_length=50)
    numero_habitantes = models.PositiveIntegerField()

    def __str__(self) -> str:
        return "{}".format(self.nombre)
        # return super().__str__()

    class Meta:
        db_table = 'pais'


class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    alcalde = models.CharField(max_length=100)
    pais = models.ForeignKey(
        Pais, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "{}".format(self.nombre, self.pais.nombre)
        # return super().__str__()

    class Meta:
        db_table = 'ciudad'

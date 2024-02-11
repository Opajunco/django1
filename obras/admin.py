from django.contrib import admin
from .models import Obra, Unit, Capitulo, PartGenDB, Zona, Fase, PartResult, PartGen, Empr
# Register your models here.

admin.site.register(Obra)
admin.site.register(Unit)
admin.site.register(Capitulo)

admin.site.register(PartGenDB)
admin.site.register(Zona)
admin.site.register(Fase)
admin.site.register(PartResult)
admin.site.register(PartGen)
admin.site.register(Empr)

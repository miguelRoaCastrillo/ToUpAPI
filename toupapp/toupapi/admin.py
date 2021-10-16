from django.contrib import admin
from toupapi.models import usuario, tema, contrato, cargo, trabajador, emprendedor

# Register your models here.
admin.site.register(usuario)
admin.site.register(tema)
admin.site.register(contrato)
admin.site.register(cargo)
admin.site.register(trabajador)
admin.site.register(emprendedor)
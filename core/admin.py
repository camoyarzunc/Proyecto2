from django.contrib import admin
from .models import Region,Comuna,Ciudad,Registro,Mascota,TipoUsuario,Estado
# Register your models here.
admin.site.register(Registro)
admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(Comuna)
admin.site.register(Mascota)
admin.site.register(TipoUsuario)
admin.site.register(Estado)


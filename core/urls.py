from django.urls import path,include
from .views import index,formulario,page,mascota,listar,page2,modificar,eliminar,registroAdoptante,listarAdop,login
urlpatterns = [ 
   path('', index,name="index"),
   path('formulario.html',formulario,name="formulario"),
   path('page.html',page,name="page"),
   path('Mascota.html',mascota,name="mascota"),
   path('listar.html',listar,name="listar"),
   path('page2.html',page2,name="page2"),
   path('modificar.html',modificar,name="modificar"),
   path('eliminar.html',eliminar,name="eliminar"),
   path('login.html',registroAdoptante,name="reAdop"),
   path('listarAdop.html',listarAdop,name="listar2"),
   path('login.hmtl',login,name='login')
]

from django.shortcuts import render
from .models import Region, Ciudad, Comuna, TipoUsuario, Estado, Mascota, Registro
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    if request.POST:
        accion = request.POST.get("Login", "")
        if accion == "Login":
            correo = request.POST.get("correo", "")
            password=request.POST.get("pass","")
            user=auth.authenticate(username=correo,password=password)
            if user is not None and user.is_active:
                auth.login(request,user)
                na=request.user.is_staff
                if na==True:
                    return render(request ,'page2.html')
                else:
                    return render(request,'page.html')
            else:
                return render(request,'login.html')
    else:
        return render(request,'login.html')

    return render(request, 'index.html')


def formulario(request):
    regiones = Region.objects.all()
    ciudades = Ciudad.objects.all()
    comunas = Comuna.objects.all()
    if request.POST:
        ingresar=request.POST.get("btnIngresar", "")
        if ingresar=="Grabar":
            rut = request.POST.get("rut", "")
            nombre = request.POST.get("nombre", "")
            apellido = request.POST.get("apellido", "")
            reg = request.POST.get("region", "")
            ciu = request.POST.get("ciudad", "")
            com = request.POST.get("comuna", "")
            correo = request.POST.get("correo", "")


            obj_region = Region.objects.get(idregion=reg)
            obj_ciudad = Ciudad.objects.get(idciudad=ciu)
            obj_comuna = Comuna.objects.get(idcomuna=com)
            regis = Registro(
                rut=rut,
                nombre=nombre,
                apellido=apellido,
                region=obj_region,
                ciudad=obj_ciudad,
                comuna=obj_comuna,
                correo=correo
            )
            
            regis.save()
            return render(request, 'formulario.html', {'reg': regiones, 'ciu': ciudades, 'com': comunas})
    else:
        return render(request, 'formulario.html', {'reg': regiones, 'ciu': ciudades, 'com': comunas})


def page(request):
    return render(request, 'page.html')


def mascota(request):

    if request.POST:
        nombre = request.POST.get("nombre", "")
        raza = request.POST.get("raza", "")
        descripcion = request.POST.get("descripcion", "")
        est = request.POST.get("estado", "")
        foto = request.POST.get("foto", "")

        masc = Mascota(
            nombre=nombre,
            raza=raza,
            descripcion=descripcion,
            estado=est,
            foto=foto
        )
        masc.save()
        return render(request, 'Mascota.html')
    else:
        return render(request, 'Mascota.html')


def listar(request):
    masc = Mascota.objects.all()
    return render(request, 'listar.html', {'mascotas': masc})


def page2(request):
    return render(request, 'page2.html')


def modificar(request):
    if request.POST:
        accion = request.POST.get("btnAccion", "")
        if accion == "Buscar":
            nom = request.POST.get("nombre", "")
            ma = Mascota.objects.get(nombre=nom)
            return render(request, 'modificar.html',
            {'ma': ma})
        if accion == "Modificar":
            nom = request.POST.get("nombre", "")
            ma = Mascota.objects.get(nombre=nom)
            raza = request.POST.get("raza", "")
            descripcion = request.POST.get("descripcion", "")
            est = request.POST.get("estado", "")

            ma.nombre = nom
            ma.raza = raza
            ma.descripcion = descripcion
            ma.estado = est
            ma.save()
            return render(request, 'modificar.html',
            {'ma': ma})
    else:
        return render(request, 'modificar.html')


def eliminar(request):


    if request.POST:
        accion=request.POST.get("btnAccion","")
        if accion == "Buscar":
                nom = request.POST.get("nombre", "")
                ma = Mascota.objects.get(nombre=nom)
                return render(request, 'eliminar.html',
                {'ma': ma})
        if accion=="Eliminar" :     
            nom=request.POST.get("nombre","")
            ma=Mascota.objects.get(nombre=nom)
            ma.delete()
            resp=True
            return render(request,'eliminar.html',{'ma':ma })
    else:
        return render(request,'eliminar.html')
def login(request):
    if request.POST:
        accion=request.POST.get("btnAccion","")
        if accion == "Ingresar":
            correo=request.POST.get("correo","")
            password=request.POST.get("pass","")
            user=auth.authenticate(username=correo,password=password)
            if user is not None and user.is_active:
                auth.login(request,user)
                na=request.user.is_staff
                if na==True:
                    return render(request ,'page2.html')
                else:
                    return render(request,'page.html')
            else:
                return render(request,'login.html')
    else:
        return render(request,'login.html')
def registroAdministrador(request):
    if request.POST:
        nombre=request.POST.get("nombre","")
        apellido=request.POST.get("apellido","")
        correo=request.POST.get("correo","")
        password=request.POST.get("pass","")
        repassword=request.POST.get("repass","")
        usuario=request.POST.get("user","")

        usu=User.objects.create_user(
            first_name=nombre,
            last_name=apellido,
            username=usuario,
            email=correo,
            password=password
        )

        if password == repassword:
            usu.is_staff=True
            usu.save()
            return render(request,'login.html')
    else:
        return render(request,'login.html')
def registroAdoptante(request):
    if request.POST:
        nombre=request.POST.get("nombre","")
        apellido=request.POST.get("apellido","")
        correo=request.POST.get("correo","")
        password=request.POST.get("pass","")
        repassword=request.POST.get("repass","")
        usuario=request.POST.get("user","")

        usu=User.objects.create_user(
            first_name=nombre,
            last_name=apellido,
            username=usuario,
            email=correo,
            password=password
        )

        if password == repassword:
            usu.is_staff=False
            usu.save()
            return render(request,'index.html')
    else:
        return render(request,'login.html')
    
def listarAdop(request):
    masc = Mascota.objects.all()
    return render(request, 'listarAdop.html', {'mascotas': masc})

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .form import FormularioUser,ImgFormu
from .models import Imagen
from django.contrib.auth import login, logout, authenticate


def inicio(request):
    usuarios = User.objects.all()
    imagen = Imagen.objects.all()
    return render(request, 'index.html', {'usuarios': usuarios,'imagenes':imagen})


def registro_usuario(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                usuario = User.objects.create_user(username=request.POST['username'],
                                                   password=request.POST['password1'])
                usuario.save()
                return redirect('/')
            except:
                return 'error de la base de datos'

        return 'las contraseñas no coinciden'
    else:
        return render(request, 'insertar_usuario.html', {'form': UserCreationForm})


def actualizar(request, id):
    usuario = request.user
    
    formu = FormularioUser(instance=usuario)
    if formu.is_valid and request.POST:
        formu = FormularioUser(request.POST, instance=usuario)
        formu.save()
        return redirect('/')
    return render(request, 'actualizar.html', {'formu': formu, 'usuario': usuario})


def eliminarusuario(request, id):
    usuario = User.objects.get(id=id)
    usuario.delete()
    return redirect('/')


def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST.get('nombre')
        password = request.POST.get('contraseña')
        usuario = User.objects.get(username=username)
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')

    return render(request, 'iniciar_sesion.html')


def cerrar_sesion(request):
    logout(request)
    return redirect('/')

# cambiar contraseña de usuario
def cambiar_contraseña(request,id):
    contraseña = request.POST.get('contraseña')
    user = User.objects.get(id=id)
    user.set_password(contraseña)
    user.save()
    return render(request,'cambiar_contraseña.html')


def agregar_imagen(request,id):
    if request.method == 'POST':
        form = ImgFormu(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'agregar_imagen.html',{'form':ImgFormu()})
    
  


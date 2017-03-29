#coding: utf8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import MyAuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from saf.models import *

def index(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/saf/')
	form = MyAuthenticationForm()
	return render(request, 'form_login.html', {'form': form})

def log_out(request):
	logout(request)
	return HttpResponseRedirect('/')

def log_in(request):
	if request.method == 'POST':
		form = MyAuthenticationForm(data=request.POST)
		
		if form.is_valid():
			user = authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/saf/')
				else:
					return HttpResponse('El usuario ha sido desactivado')
			else:
				return HttpResponse('Usuario y contraseña invalidos')
		else:
			return render(request, 'form_login.html', {'form': form})
	else:
		return HttpResponse('No seas travieso')


def registro(request):
    if request.method == 'POST':
        form = MyAuthenticationForm(request.POST, request.FILES)
        #if form.is_valid():
        contrasena = request.POST.get('password')
        usuario = request.POST.get('username')
        nombres = request.POST.get('first_name')
        apellidos = request.POST.get('last_name')
        email = request.POST.get('email')
        sexo = request.POST.get('sex')
        dia = request.POST.get('day')
        mes = request.POST.get('month')
        anio = request.POST.get('year')
        is_staff = False 
        is_active = True 
        is_superuser = False
        usuario = User.objects.create(
            password = contrasena,
            is_superuser = is_superuser,
            username = usuario,
            is_staff =is_staff,
            is_active = is_active
        )
        try:
            usr = MyPerfil(nombreUsuario = usuario, nombre = nombres, apellido = apellidos, sexo_id = sexo, correo = email, fechaNacimiento = str(anio+"-"+mes+"-"+dia))
            usr.save()
            return HttpResponseRedirect('/saf/')
        except Exception as e:
            return HttpResponse(e)

    else:
        form = MyAuthenticationForm()
    context = {'form': form}
    return render(request, 'index.html', context)
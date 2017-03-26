from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Count
from .models import MyPerfil, NotificacionA

def index(request):
	data = MyPerfil.objects.filter(nombreUsuario = request.user.username).get()
	
	ctx = {'perfil' : data}
	return render(request, "index.html", ctx)

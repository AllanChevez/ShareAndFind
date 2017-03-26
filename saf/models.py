from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

@python_2_unicode_compatible
class Sexo(models.Model):
	nombre = models.CharField(max_length=25)

	def __str__(self):
		return self.nombre

@python_2_unicode_compatible
class MyPerfil(models.Model):
	nombreUsuario = models.CharField(max_length=25, primary_key=True)
	nombre = models.CharField(max_length=25)
	apellido = models.CharField(max_length=25) 
	sexo = models.ForeignKey(Sexo)
	correo = models.EmailField()
	fechaNacimiento = models.DateField()
	Avatar = models.ImageField(upload_to = "media/Avatar", null=True, blank =True)

	def __str__(self):
		return self.nombreUsuario

@python_2_unicode_compatible
class Rol(models.Model):
	codigo = models.IntegerField()
	nombre = models.CharField(max_length=25)

	def __str__(self):
		return self.nombre

@python_2_unicode_compatible
class Contacto(models.Model):
	nombreContacto = models.CharField(max_length=25)
	nombreUsuario = models.ForeignKey(MyPerfil)
	rol = models.ForeignKey(Rol)
	fechaAmistad = models.DateField()

	def __str__(self):
		return self.nombreContacto

@python_2_unicode_compatible
class NotificacionA(models.Model):
	nombreContacto = models.ForeignKey(Contacto)
	nombreUsuario = models.CharField(max_length=25)
	Decicion = models.IntegerField()

	def __str__(self):
		return self.nombreContacto.nombreContacto

@python_2_unicode_compatible
class Categoria(models.Model):
	nombre = models.CharField(max_length=25)

	def __str__(self):
		return self.nombre

@python_2_unicode_compatible
class Documento(models.Model):
	nombre = models.CharField(max_length=25)
	archivo = models.FileField(upload_to = "media/archivo")
	categoria = models.ForeignKey(Categoria)
	nombreUsuario = models.ForeignKey(MyPerfil)

	def __str__(self):
		return self.nombre

@python_2_unicode_compatible
class NotificacionD(models.Model):
	NombreDocumento = models.ForeignKey(Documento)
	usuarioDescarga = models.CharField(max_length=25)

	def __str__(self):
		return str(self.NombreDocumento)


@python_2_unicode_compatible
class Publicacion(models.Model):
	nombreUsuario = models.ForeignKey(MyPerfil)
	descripcion = models.TextField()
	fecha_Publicacion = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.nombreUsuario.nombreUsuario.username


@python_2_unicode_compatible
class Comentario(models.Model):
	publicacion = models.ForeignKey(Publicacion)
	contenido = models.TextField(max_length=141)
	usuario = models.CharField(max_length=25)
	fecha_Publicacion = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.contenido


@python_2_unicode_compatible
class NotificacionC(models.Model):
	usuarioComentado = models.ForeignKey(Comentario)
	usuarioComenta = models.CharField(max_length=25)

	def __str__(self):
		return self.usuarioComentado.contenido


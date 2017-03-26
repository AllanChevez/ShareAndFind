from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^login/$', views.log_in, name='login'),
	url(r'^registro/$', views.registro, name='registro'),
]
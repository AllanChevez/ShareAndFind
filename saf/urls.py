from django.conf.urls import url
from . import views
#se mandan a llamar las urls creadas en el proyecto
urlpatterns = [
	url(r'^$', views.index, name='index'),
	

]
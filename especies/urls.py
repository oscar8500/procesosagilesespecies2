from django.conf.urls import url

from . import views

urlpatterns = [
    # Peticiones Ajax o  JavaScript
    url(r'^addUser/$', views.adicionar_usuario, name='addUser'),
    url(r'^logout/$', views.logout_request, name='logout'),
    url(r'^isLogged/$', views.islogged, name='isLogged'),
    url(r'^login/$', views.login_request, name='login'),
    url(r'^fillCities/$', views.fillCities, name='fillCities'),

    # Peticiones a vistas
    url(r'^$', views.index_especies, name=''),
    url(r'^agregarUsuario/$', views.index_usuario, name='agregarUsuario'),
    url(r'^ingresar/$', views.ingresar, name='ingresar'),
    url(r'^detalle/([0-9])/$', views.detalleEspecie, name='detalle'),
]

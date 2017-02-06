from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^addUser/$', views.adicionar_usuario, name='addUser'),

    url(r'^listar/$', views.index_especies, name='listar'),
    url(r'^agregarUsuario/$', views.index_usuario, name='agregarUsuario'),
]

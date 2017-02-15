from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db.models import signals
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Country(models.Model):
    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'
    code = models.CharField(max_length=200, blank=False, null=True, verbose_name="Codigo de Pais")
    name = models.CharField(max_length=200, blank=False, null=True, verbose_name="Nombre de Pais")
    def __unicode__(self):
       return 'Pais: ' +str(self.code)+'-'+ self.name
    def nomcorto(self):
        return self.name



class City(models.Model):
    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
    name = models.CharField(max_length=200, blank=False, verbose_name="Nombre de Ciudad")
    country = models.ForeignKey(Country, blank=False, null=True, on_delete=models.CASCADE, verbose_name="Seleccion de Pais")
    def __unicode__(self):
       return 'Ciudad: ' + self.name+'-'+Country.nomcorto(self.country)
    def nomCorto(self):
        return self.name+'-'+Country.nomcorto(self.country)


class UserProfile(models.Model):
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    imageFile = models.ImageField(upload_to='images', null=True, verbose_name= "Imagen")
    description = models.TextField(max_length=1000, default='',verbose_name="Descripcion")
    city_name = models.CharField(max_length=100, default='Bogota',verbose_name="Ciudad",editable=False)
    country_name = models.CharField(max_length=100, default='Colombia',verbose_name="Pais",editable=False)
    city = models.ForeignKey(City, blank=False, null=True, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    def __unicode__(self):
       return 'Usuario: '+self.user.username


class Category(models.Model):
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    name = models.CharField(max_length=100)
    def __unicode__(self):
       return 'Categoria: ' + self.name
    def nomCorto(self):
        return self.name


class Specie(models.Model):
    class Meta:
        verbose_name = 'Especie'
        verbose_name_plural = 'Especies'
    name = models.CharField(max_length=100,verbose_name="Nombre Comun")
    category = models.ForeignKey(Category,blank=False,null=True,on_delete=models.CASCADE,verbose_name="Categoria")
    kingdom=models.CharField(max_length=100, default='',verbose_name="Reino")
    phylum=models.CharField(max_length=100, default='',verbose_name="Filo")
    classEspecie = models.CharField(max_length=100, default='',verbose_name="Clase")
    order = models.CharField(max_length=100, default='',verbose_name="Orden")
    family = models.CharField(max_length=100, default='',verbose_name="Familia")
    genus = models.CharField(max_length=100, default='',verbose_name="Genero")
    species=models.CharField(max_length=100, default='',verbose_name="Nombre Cientifico")
    imageFile = models.ImageField(upload_to='images', null=True,verbose_name="Imagen")
    short_desc = models.CharField(max_length=200, default='',verbose_name="Descripcion Corta")
    large_desc = models.TextField(max_length=2000, default='',verbose_name="Descripcion Larga")
    def __unicode__(self):
       return 'Nombre: ' + self.name

class Comment(models.Model):
    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
    content = models.TextField(max_length=1000)
    email = models.EmailField(max_length=50)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='comments')
    specie = models.ForeignKey(Specie, on_delete=models.CASCADE, related_name='comments')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db.models import signals
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Country(models.Model):
    code = models.CharField(max_length=200, blank=False)
    name = models.CharField(max_length=200, blank=False)


class City(models.Model):
    name = models.CharField(max_length=200, blank=False)
    country = models.ForeignKey(Country, null=True)

class UserProfile(models.Model):
    imageFile = models.ImageField(upload_to='images', null=True)
    city = models.ForeignKey(City, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    description = models.TextField(max_length=1000,default='')
    city = models.CharField(max_length=100,default='Bogota')
    country= models.CharField(max_length=100,default='Colombia')

class Specie(models.Model):
    name= models.CharField(max_length=100)
    category= models.CharField(max_length=100,default='')
    tax_clasification= models.CharField(max_length=100,default='')
    scientific_name= models.CharField(max_length=100,default='')
    imageFile = models.ImageField(upload_to='images', null=True)
    short_desc=models.CharField(max_length=200,default='')
    large_desc= models.TextField(max_length=2000,default='')

class Comment(models.Model):
    content= models.TextField(max_length=1000)
    email= models.EmailField(max_length=50)
    user= models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='comments')
    specie= models.ForeignKey(Specie, on_delete=models.CASCADE, related_name='comments')



class Category(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



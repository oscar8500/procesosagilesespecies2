import json

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.core import serializers
from django.http import JsonResponse

# Create your views here.
from .models import UserProfile, Country, City, Specie


@csrf_exempt
def adicionar_usuario(request):
    mensaje = ''

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        email = request.POST['email']
        description = request.POST['description']
        user_name = email

        usuarios = User.objects.filter(username=email)
        if usuarios is not None and usuarios.count() > 0:
            mensaje = 'El usuario ya existe en el sistema'
        else:
            user_model = User.objects.create_user(username=user_name, password=password)
            user_model.first_name = first_name
            user_model.last_name = last_name
            user_model.email = email
            user_model.profile.description = description
            user_model.profile.imageFile = request.FILES['imageFile']
            id_city = request.POST['id_city']
            user_model.profile.city_id = id_city
            city_name = City.objects.values_list('name', flat=True).get(pk=id_city)
            country_id = City.objects.values_list('country_id', flat=True).get(pk=id_city)
            user_model.profile.city_name = city_name
            country_name = Country.objects.values_list('name', flat=True).get(pk=country_id)
            user_model.profile.country_name = country_name

            user_model.save()
            mensaje = 'ok'

    return JsonResponse({"mensaje": mensaje})


@csrf_exempt
def login_request(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        username = jsonUser['username']
        password = jsonUser['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            mensaje = 'ok'
        else:
            mensaje = 'Nombre de usuario o clave no valido'

    return JsonResponse({"mensaje": mensaje})


@csrf_exempt
def logout_request(request):
    logout(request)
    return JsonResponse({"mensaje": 'ok'})


@csrf_exempt
def islogged(request):
    if request.user.is_authenticated():
        mensaje = 'ok'
    else:
        mensaje = 'no'

    return JsonResponse({"mensaje": mensaje})


@csrf_exempt
def fillCities(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        id_country = jsonUser['id_country']
        cities = City.objects.filter(country_id=id_country)
        citiesDict = dict([(c.id, c.name) for c in cities])

    return HttpResponse(json.dumps(citiesDict))


def index_especies(request):
    lista_especies = Specie.objects.all()
    context = {'lista_especies': lista_especies}
    return render(request, 'especies/index.html', context)


def index_usuario(request):
    lista_paises = Country.objects.all()
    context = {'lista_paises': lista_paises}
    return render(request, 'especies/registro.html', context)


def ingresar(request):
    return render(request, 'especies/login.html')

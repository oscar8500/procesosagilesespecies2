import json

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.core import serializers
from django.http import JsonResponse

# Create your views here.
from especies.models import UserProfile


@csrf_exempt
def adicionar_usuario(request):
    if request.method == 'POST':
        json_user = json.loads(request.body)
        first_name = json_user['first_name']
        last_name = json_user['last_name']
        password = json_user['password']
        email = json_user['email']
        user_name = email

        user_model = User.objects.create_user(username=user_name, password=password)
        user_model.first_name = first_name
        user_model.last_name = last_name
        user_model.email = email
        user_model.profile.imageFile = json_user['image_file']

        user_model.save()

    return HttpResponse(serializers.serialize("json", [user_model]))


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


def index_especies(request):
    return render(request, 'especies/index.html')


def index_usuario(request):
    return render(request, 'especies/registro.html')


def ingresar(request):
    return render(request, 'especies/login.html')

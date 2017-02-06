import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.core import serializers


# Create your views here.

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
        user_model.save()

    return HttpResponse(serializers.serialize("json", [user_model]))


def index_especies(request):
    return render(request, 'especies/index.html')


def index_usuario(request):
    return render(request, 'especies/registro.html')

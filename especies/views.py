import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


from .models import Country, City, Specie, Category, Comment


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
def editar_usuario(request):
    mensaje = ''

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        description = request.POST['description']
        user_model= request.user
        user_model.first_name = first_name
        user_model.last_name = last_name
        user_model.profile.description = description
        if request.FILES.get('imageFile', False) :
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
    else:
        lista_paises = Country.objects.all()
        context = {'lista_paises': lista_paises,
                   'user_model': request.user,
                   'user_profile':request.user.profile}
        return render(request, 'especies/modificacion.html', context)

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
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        id_categoria = jsonUser['id_categoria']
        lista_especies = Specie.objects.filter(category_id=id_categoria)
    else:
        lista_especies = Specie.objects.all()
    lista_categorias = Category.objects.all()

    context = {
        'lista_especies': lista_especies,
        'lista_categorias': lista_categorias
    }
    return render(request, 'especies/index.html', context)


def index_filter(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        id_categoria = jsonUser['id_categoria']
        lista_especies = Specie.objects.filter(category_id=id_categoria)
    else:
        lista_especies = Specie.objects.all()
    especiesDict = dict([(c.id, c.name) for c in lista_especies])
    return HttpResponse(json.dumps(especiesDict))

def index_usuario(request):
    lista_paises = Country.objects.all()
    context = {'lista_paises': lista_paises}
    return render(request, 'especies/registro.html', context)


def details_specie(request):
    json


def ingresar(request):
    return render(request, 'especies/login.html')


def detalleEspecie(request, id):
    especie = Specie.objects.get(id=id)
    comments = Comment.objects.filter(specie=especie)

    context = {
        'especie': especie,
        'comments': comments
    }


    return render(request, 'especies/detailspecie.html', context)

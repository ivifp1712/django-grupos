from this import d
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from gestionAlumnos.models import Alumnos
from django.contrib.auth.models import *
import random
from django.contrib.sessions.models import Session
from django.db.models import Q



def mezclar_lista(lista_original):
    lista = lista_original[:]
    longitud_lista = len(lista)
    for i in range(longitud_lista):
        indice_aleatorio = random.randint(0, longitud_lista - 1)
        temporal = lista[i]
        lista[i] = lista[indice_aleatorio]
        lista[indice_aleatorio] = temporal
    return lista
# Create your views here.

# def busqueda_alumno(request):

#     return render(request, 'busqueda.html')

# def introducido (request):
#     if request.method == 'POST':
#         name = request.POST['nombre']
#         al = Alumnos(nombre=name)
#         bus = Alumnos.objects.filter(nombre__iexact=name)
#         if bus:
#             return HttpResponse("""Ese nombre ya ha sido introducido. <button onclick="window.location.href = '/introducir/'"> Volver</button>""")
#         else: 
#             al.save()
#             return HttpResponse("<script>window.location.href = '/introducir/'</script>")
# def introducir (request):
#     return render(request, 'introducir.html')

def todos(request):
    alertas = ""
    #alertas = f"{request.user.is_authenticated}"
    if request.user.is_authenticated == False:
        #alertas = "No estas logueado"
        return redirect('/login/')
    todos1 = User.objects.filter(~Q(username__icontains="ivi"))
    todos = []
    for x in todos1:
        todos.append(x.first_name)
    todos.sort()
    #   todos = User.objects.filter(~Q(username="ivi"))

    if 'reload' in request.POST:
        return render(request, 'todos.html', {"todos": todos, "alertas": alertas})


    if 'nombre' in request.POST:
        name = request.POST['nombre']
        bus = User.objects.filter(first_name__iexact=name)
        if not bus:
            username = ""
            for y in range(len(name)):
                if name[y] != " ":
                    #print(x[y])
                    username += name[y]
                else:
                    break
            username += "."
            
            for z in range(3):
                    username += name[z+y+1]
            user = User.objects.create_user(username, '', 'campusfp')
            user.first_name = str(name)
            user.save()
            alertas = "Alumno registrado correctamente!"
        else:
            alertas = "Alumno ya existente!"

    if 'nombre1' in request.POST:
        name = request.POST['nombre1']
        dele = User.objects.filter(first_name__iexact=name)
        if dele:
            dele.delete()
            alertas = "Alumno eliminado correctamente!"
        else:
            alertas = "No se ha podido eliminar ese alumno!"
        

    if 'num' in request.POST:
        todos1 = mezclar_lista(list(todos))
        num = int(request.POST['num'])
        grupos = [todos1[i:i + num] for i in range(0, len(todos1), num)] 
        return render(request, 'todos.html', {"todos": todos, "grupos": grupos, "num": request.POST['num']})

    return render(request, 'todos.html', {"todos": todos, "alertas": alertas})



def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'register.html')

# def register(request):
#     if 'email' in request.POST and 'user' in request.POST and 'pass' in request.POST:
#         #return HttpResponse(f".{bus}.")
#         if User.objects.filter(username__exact=request.POST["user"]):
#             return HttpResponse(f"<h2> Usuario duplicado.</h2>")
#         else:
#             user = User.objects.create_user(request.POST["user"], request.POST["email"], request.POST["pass"])
#             user.save()
#             return HttpResponse("<h2> Usuario registrado. </h2>")
#     return HttpResponse("No funciona el formulario.")


def auth(request):
    return HttpResponse("Usuario logueado.")
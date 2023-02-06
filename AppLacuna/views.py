from django.shortcuts import render
from django.http import HttpResponse
from AppLacuna.models import *
from AppLacuna.forms import *

# Create your views here.

def inicio(request):
    return render(request,"AppLacuna/inicio.html")

def pokemon(request):
    return render(request,"AppLacuna/pokemon.html")

def entrenador(request):
    return render(request,"AppLacuna/entrenador.html")

def gym(request):
    return render(request,"AppLacuna/gym.html")

def formulario_pokemon(request):
    if request.method == "POST":

        formularioP = formularioPokemon(request.POST)

        if formularioP.is_valid():

            info = formularioP.cleaned_data
            
            pokemon = Pokemon(nombre=info["nombre"], tipo=info["tipo"], peso=info["peso"])

            pokemon.save()

            return render(request, "AppLacuna/inicio.html")
        
    else:
        formularioP = formularioPokemon()
            

    return render(request,"AppLacuna/pokemon.html", {"formp":formularioP})

def formulario_entrenador(request):
    
    if request.method == "POST":

        formularioE = formularioEntrenador(request.POST)

        if formularioE.is_valid():

            info = formularioE.cleaned_data
            
            entrenador = Entrenador(nombre=info["nombre"], edad= info ["edad"],ciudad= info["ciudad"])

            entrenador.save()

            return render(request, "AppLacuna/inicio.html")
        
    else:
        formularioE = formularioEntrenador()
            
    return render(request,"AppLacuna/entrenador.html", {"forme":formularioE})

def formulario_gym(request):
    
    if request.method == "POST":

        formularioG = formularioGym(request.POST)
        
        if formularioG.is_valid():

            info = formularioG.cleaned_data
            
            gym = Gym(nombre=info["nombre"], medalla= info ["medalla"],tipo= info["tipo"])

            gym.save()

            return render(request, "AppLacuna/inicio.html")
                
    else:
        formularioG = formularioGym()
            
    return render (request, "AppLacuna/gym.html", {"formg":formularioG})

def busquedaPokemon(request):
    return render(request, "AppLacuna/inicio.html")

def resultado(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        pokemon1 = Pokemon.objects.filter(nombre__icontains=nombre)
        return render(request, "AppLacuna/inicio.html", {"pokemon1":pokemon1, "nombre":nombre})

    else:
        
        respuesta = "no enviaste datos"
        
    return HttpResponse(respuesta)
from django.urls import path
from AppLacuna.views import *

urlpatterns = [
    path("", inicio, name = "Inicio"),
    path("pokemones/", pokemon, name ="Pokemon"),
    path("Entrenadores/", entrenador, name = "Entrenador"),
    path("GYMS/", gym, name = "GYM"),
    path("formularioEntrenador/", formulario_entrenador, name = "entrenadorFormulario"),
    path("formularioPokemon/", formulario_pokemon, name = "pokemonFormulario"),
    path("formularioGym/", formulario_gym, name = "gymFormulario"),
    path("buscar/", busquedaPokemon, name="busquedapokemon"),
    path("respuesta/",resultado, name= "Respuesta"),
]
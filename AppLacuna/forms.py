from django import forms


class formularioPokemon(forms.Form):
    nombre = forms.CharField()
    tipo = forms.CharField()
    peso = forms.IntegerField()
    
class formularioEntrenador(forms.Form):
    nombre = forms.CharField()
    edad = forms.IntegerField()
    ciudad = forms.CharField()
    
class formularioGym(forms.Form):
    nombre = forms.CharField()
    medalla = forms.CharField()
    tipo = forms.CharField()

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return render(request, 'cs3team1/home.html')

def ingredient(request):
	return render(request, 'cs3team1/ingredients.html')

def menu(request):
	return render(request, 'cs3team1/menu.html')

def recommendation(request):
	return render(request, 'cs3team1/recommendation.html')

def recipe(request):
	return render(request, 'cs3team1/recipe.html')
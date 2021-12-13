from django.shortcuts import render
from django.http import HttpResponse
from django .views.generic import View
from .models import Post
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

class IndezView(View):
	def get(self, request, *args, **kwargs):
		post_data = Post.objects.order_by('-id')
		return render(request, 'cs3team1/menu.html', {
			'post_data': post_data
		})

def update_ingredients(request, ingredients_id):
	return HttpResponse("ingredients_id: {}".format(ingredients_id))

def update_recipe(request, recipe_id):
	return HttpResponse("recipe_id: {}".format(recipe_id))
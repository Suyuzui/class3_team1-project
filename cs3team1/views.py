from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from cs3team1.models import Post
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
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

class IndexView(View):
	def get(self, request, *args, **kwargs):
		post_data = Post.objects.order_by('-id')
		return render(request, 'cs3team1/menu.html', {
			'post_data': post_data
		})

def update_ingredients(request, ingredients_id):
	return HttpResponse("ingredients_id: {}".format(ingredients_id))

def update_recipe(request, recipe_id):
	return HttpResponse("recipe_id: {}".format(recipe_id))

class PostDetailView(View):
	def get(self, request, *args, **kwargs):
		post_data = Post.objects.get(id=self.kwargs['pk'])
		return render(request, 'cs3team1/post_detail.html', {
			'post_data': post_data
		}) 

class CreatePostView(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		form = PostForm(request.POST or None)

		if form.is_valid():
			post_data = Post()
			post_data.author = request.user
			post_data.title = form.cleaned_data['title']
			post_data.content = form.cleaned_data['content']
			post_data.save()
			return redirect('post_detail', post_data.id)

		return render(request, 'cs3team1/post_form.html',{
			'form': form
		})

class PostEditView(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		post_data = Post.objects.get(id=self.kwargs['pk'])
		form = PostForm(
			request.POST or None,
			initial= {
				'title':post_data.title,
				'content':post_data.content
			}
		)	
		return render(request, 'cs3team1/post_form.html',{
			'form': form
		})
	
	def post(self, request, *args, **kwargs):
		form = PostForm(request.POST or None)

		if form.is_valid():
			post_data = Post.objects.get(id=self.kwargs['pk'])
			post_data.title = form.cleaned_data['title']
			post_data.content = form.cleaned_data['content']
			post_data.save()
			return redirect('post_detail', self.kwargs['pk'])

		return render(request, 'cs3team1/post_form.html',{
			'form': form
		})

class PostDeleteView(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		post_data = Post.objects.get(id=self.kwargs['pk'])	
		return render(request, 'cs3team1/post_delete.html', {
			'post_data': post_data
		}) 

	def post(self, request, *args, **kwargs):
		post_data = Post.objects.get(id=self.kwargs['pk'])
		post_data.delete()
		return redirect('index') 	

def accounts(request):
	return render(request, 'menu/accounts/login.html')

def allauth(request):
	return render(request, 'menu/accounts/login.html')
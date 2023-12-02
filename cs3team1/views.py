from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from .models import Post ,Category
#from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, query
from functools import reduce
from operator import and_
# Create your views here.
#def home(request):
#return render(request, 'cs3team1/home.html')

def ingredient(request):
	return render(request, 'cs3team1/ingredients.html')

#def jQueryPost(request):
	return redirect('https://code.jquery.com/jquery-3.4.1.min.js')

def recommendation(request):
	context = {
		"id": 1,
		"title": "白菜と豚肉のレモン炒め",
		"body": "sample"
	}
	return render(request, 'cs3team1/recommendation.html', context)

def recipe(request):
	context = {
		"id": 1,
		"title": "白菜と豚肉のレモン炒め",
		"ingredients": ["白菜:中4枚", "豚ロース:薄切り100g", "長ねぎ:40g", "赤パプリカ:30g"],
		"seasonings": ["サラダ油:小さじ1", "レモン汁:1/2個分", "にんにくすりおろし:小さじ1", "塩:小さじ1/3", "粗びき黒こしょう:少々", "ごま油:小さじ1"],
		"howto": ["白菜は縦に4等分にして3cmの長さに切る。豚肉はこま切りに、長ねぎはみじん切り、パプリカは千切りに切っておく。", "【調味料】の材料をよく混ぜ合わせておく。", "フライパンにサラダ油を入れて熱し、中火で豚肉を炒める。火が通ったら白菜を入れて炒め合わせる。", "白菜がしんなりしてきたら、2の【調味料】を回しかけ、みじん切りにした長ねぎを入れて炒める。", "長ねぎに火が通ったら、最後にパプリカを入れて軽く混ぜ合わせ、器に盛り付ける。"],
		"memo": "白菜はくせが無く、おひたしや漬物、鍋の食材など調理方法もさまざまです。今回は減塩になるようレモン汁を使ってさっぱりと仕上げてみました。95％が水分で栄養価は高くないのですが、ビタミンC、カリウムなどが含まれていて利尿作用や美肌効果があります。",
		"nutrition_facts_label": ["カロリー:110", "タンパク質:5.6", "脂質:7.9", "塩分:0.5"]
	}
	return render(request, 'cs3team1/recipe.html', context)

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

#class CreatePostView(LoginRequiredMixin, View):
	#def get(self, request, *args, **kwargs):
	#	form = PostForm(request.POST or None)

#		return render(request, 'cs3team1/post_form.html',{
#			'form': form
#		})
	
#	def post(self, request, *args, **kwargs):
#		form = PostForm(request.POST or None)

#		if form.is_valid():
#			post_data = Post()
#			post_data.author = request.user
#			post_data.title = form.cleaned_data['title']
#			category = form.cleaned_data['category']
#			category_data = Category.objects.get(name=category)
#			post_data.category = category_data
#			post_data.content = form.cleaned_data['content']
#			if request.FILES:
#				post_data.image = request.FILES.get('image')
#			post_data.save()
#			return redirect('post_detail', post_data.id)
#		return render(request, 'cs3team1/post_form.html',{
#			'form': form
#		})		


#class PostEditView(LoginRequiredMixin, View):
#	def get(self, request, *args, **kwargs):
#		post_data = Post.objects.get(id=self.kwargs['pk'])
#		form = PostForm(
#			request.POST or None,
#			initial= {
#				'title':post_data.title,
#				'category':post_data.category,
#				'content':post_data.content,
#				'image':post_data.image
#			}
#		)	
#		return render(request, 'cs3team1/post_form.html',{
#			'form': form
#		})
#	def post(self, request, *args, **kwargs):
#		form = PostForm(request.POST or None)
#
#		if form.is_valid():
#			post_data = Post.objects.get(id=self.kwargs['pk'])
#			post_data.author = request.user
#			post_data.title = form.cleaned_data['title']
#			category = form.cleaned_data['category']
#			category_data = Category.objects.get(name=category)
#			post_data.category = category_data
#			post_data.content = form.cleaned_data['content']
#			if request.FILES:
#				post_data.image = request.FILES.get('image')
#			post_data.save()
#			return redirect('post_detail', self.kwargs['pk'])
#		return render(request, 'cs3team1/post_form.html',{
#			'form': form
#		})

class PostDeleteView(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		post_data = Post.objects.get(id=self.kwargs['pk'])	
		return render(request, 'cs3team1/post_delete.html', {
			'post_data': post_data
		}) 

	def post(self, request, *args, **kwargs):
		post_data = Post.objects.get(id=self.kwargs['pk'])
		post_data.delete()
		return redirect('home') 	

class CategoryView(View):
	def get(self, request, *args, **kwargs):
		category_data =Category.objects.get(name=self.kwargs['category'])
		post_data = Post.objects.order_by('-id').filter(category=category_data)
		return render(request, 'cs3team1/menu.html', {
			'post_data': post_data
		})

class SearchView(View):
	def get(self, request, *args, **kwargs):
		post_data = Post.objects.order_by('-id')
		keyword = request.GET.get('keyword')

		if keyword:
			exclusion_list = set([' ', ' '])
			query_list = ''
			for word in keyword:
				if not word in exclusion_list:
					query_list += word
			query = reduce(and_, [Q(title__icontains=q) | Q(content__icontains=q) for q in query_list])
			post_data = post_data.filter(query)

		return render(request, 'cs3team1/menu.html', {
			'keyword': keyword,
			'post_data': post_data
		})
 
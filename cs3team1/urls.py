from django.urls import path
from cs3team1 import views

urlpatterns = [
    #path('', views.home, name='home'),
    path('', views.IndexView.as_view(),name='home'),
    #path('', views.ingredient, name='ingredient'),
    path('ingredients', views.ingredient, name='ingredient'),
    path('recommendation', views.recommendation, name='recommendation'),
    path('recipe', views.recipe, name='recipe'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    #path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    #path('post/<int:pk>/edit/', views.PostEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('category/<str:category>', views.CategoryView.as_view(), name='category'),
    path('search', views.SearchView.as_view(), name='search'),
    #path('', views.jQueryPost, name='ingredientJQuery')
]
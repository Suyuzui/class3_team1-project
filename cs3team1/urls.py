from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('', views.ingredient, name='ingredient'),
    path('ingredients', views.ingredient, name='ingredient'),
    #path('menu', views.menu, name='menu'),
    path('recommendation/<int:ingredients_id>', views.recommendation, name='recommendation'),
    #path('recipe/<int:recipe_id>', views.recipe, name='recipe'),
    path('menu', views.IndexView.as_view(), name='index'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.PostEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('', views.ingredient, name='ingredient'),
    path('ingredients', views.ingredient, name='ingredient'),
    path('menu', views.menu, name='menu'),
    path('recommendation/<int:ingredients_id>', views.recommendation, name='recommendation'),
    path('recipe', views.recipe, name='recipe'),
    path('menu', views.IndexView.as_view(), name='index'),
    path('menu/post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('menu/post/new', views.CreatePostView.as_view(), name='post_new'),
    path('menu/post/<int:pk>/edit/', views.PostEditView.as_view(), name='post_edit')
]
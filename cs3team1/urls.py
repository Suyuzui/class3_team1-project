from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('', views.ingredient, name='ingredient'),
    path('ingredients', views.ingredient, name='ingredient'),
    path('menu', views.menu, name='menu'),
    path('recommendation/<int:ingredients_id>', views.recommendation, name='recommendation'),
    path('recipe', views.recipe, name='recipe'),
]
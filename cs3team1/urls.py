from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ingredients', views.ingredient, name='ingredient'),
    path('menu', views.menu, name='menu'),
    path('recommendation', views.recommendation, name='recommendation'),
    path('recipe', views.recipe, name='recipe'),
]
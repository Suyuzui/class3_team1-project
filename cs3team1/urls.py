from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.ingredient, name='ingredient'),
    path('menu', views.menu, name='menu'),
    path('recommendation/<int:>', views.recommendation, name='recommendation'),
    path('recipe/<int:>', views.recipe, name='recipe'),
]
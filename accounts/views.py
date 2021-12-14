from django.shortcuts import render, redirect
from allauth.account import views
from django.views.generic.base import TemplateView

class LoginView(views.LoginView):
    template_name = 'menu/accounts/login.html'
# Create your views here.

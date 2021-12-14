from django.urls import path
from accounts import views

urlpatterns =[
    path('menu/login/', views.LoginViews.as_view(), name='account_login'),
]
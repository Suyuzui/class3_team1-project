"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from cs3team1 import views as cs3team1_views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', include('cs3team1.urls')),
    path('ingredients',cs3team1_views.ingredient,name='ingredient'),
    path('recommendation', include('cs3team1.urls') ),
    path('recipe', include('cs3team1.urls') ),
    path('admin/',admin.site.urls),
    path('accounts/', include('cs3team1.urls') ),
    path('accounts/', include('allauth.urls') ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


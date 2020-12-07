"""movie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage),
    path('login/',login1),
    path('signup/',signup1),
    path('homepage/',homepage1),
    path('addmovie/',addmovie1),
    path('listofmovies',listofmovies1),
    path('addtiming/<int:id>',addtiming),
    path('availableticket',availableticket1),
    path('purchaseticket/<int:id>',purchaseticket1)
]

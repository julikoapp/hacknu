"""
URL configuration for epam_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    # path("garbage/", include("garbage.urls")),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path('api/', include('garbage.urls'))
    # path("client/", include("client.urls")),
    # path("brigada/", include("brigada.urls")),
    # path("operator/", include("operator.urls"))
]

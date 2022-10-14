"""MyProfiles URL Configuration

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
from django.urls import path, re_path
from Index import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^add$', views.add, name = "add"),
    re_path(r'^login/$', views.login, name = "login"),
    re_path(r'^register/$', views.register, name = "register"),
    re_path(r'^list/$', views.list_sites, name = "list"),
    re_path(r'^remove/$', views.remove, name='remove'),
    re_path(r'^contact/$', views.contact, name='contact'),
    re_path(r'^privacy/$', views.privacy, name='privacy'),
    re_path(r'^terms/$', views.terms, name='terms'),
    re_path(r'^login/$', views.login, name='login')
]

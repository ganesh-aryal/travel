"""travel URL Configuration

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
from app import views

urlpatterns = [
   
    path('',views.home),
    path('signin',views.signin),
    path('form',views.signup),
    path('entry',views.entry),
    path('package',views.package),
    path('dash',views.index),
    path('search',views.search),
    path('index2',views.index2),
    path('User',views.index),
    path('layout',views.layout),
    path('booking',views.booking),
    path('edituser/<int:id>',views.edituser),
    path('updateuser/<int:id>',views.updateuser),
    path('deleteuser/<int:id>',views.deleteuser),
    path('package',views.package),
    path('createuser',views.createuser),
    path('createpackage',views.createpackage),
    path('editpackage/<int:id>',views.editpackage),
    path('upadatepackage/<int:id>',views.updatepackage),
    path('deletepackage/<int:id>',views.deletepackage),
    path('customer',views.customer),
    path('createcustomer',views.createcustomer),
    path('editcustomer/<int:id>',views.editcustomer),
    path('updatecustomer/<int:id>',views.updatecustomer),
    path('deletecustomer/<int:id>',views.deletecustomer),

    path('book',views.book),
    path('book_delete/<int:id>',views.book_delete),
    path('createcustomer_self',views.createcustomer_self)
   
]

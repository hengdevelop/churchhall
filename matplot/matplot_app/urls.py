from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homes, name ="homes"),
	path('aboutme', views.aboutme, name ="aboutme")


]

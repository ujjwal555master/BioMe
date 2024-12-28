from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path("", views.index, name='home'),
    path("blogpost/<int:id>", views.blogpost, name="blogHome")

]
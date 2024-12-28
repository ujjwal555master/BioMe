from django.contrib import admin
from django.urls import path, include
from shop import views

urlpatterns = [
    path("", views.index, name='home'),
    path("task/", views.task, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),

]
from django.contrib import admin
from django.urls import path
from movie import views

urlpatterns = [
    path('',views.homepage),
    ]
from django.contrib import admin
from django.shortcuts import render , redirect
from django.urls import path
from users import views
from .views import all_details_pdf

app_name = 'users'

urlpatterns = [
    path('', views.homepage, name='home'),
    path('homepage/',views.homepage, name= 'homepage'),
    path('entry/', views.Entry, name='entry'),
    path('registration/', views.registration, name= 'registration'),
    path('all_details_pdf/',views.all_details_pdf, name='all_details_pdf'),



] 



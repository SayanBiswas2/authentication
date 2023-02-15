from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
  path('',views.home),
  path('login/',views.login),
  path('signup/',views.signup),
  path('loginapi/',views.loginapi),
  path('signupapi/',views.signupapi),
]
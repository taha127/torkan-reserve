from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name='home'),
    path('register/', views.phone_number_view, name='register'),
    path('register/code/' , views.verify, name='code_view'),
    path('register/code/welcome' ,views.welcome, name='welcome')


]
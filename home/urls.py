from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name='home'),
    path('register/', views.phone_number_view, name='register'),
    path('register/code/' , views.phone_number_view, name='code_view')


]
from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name='home'),
    path('', views.home, name='home'),
    path('register/', views.phone_number_view, name='register'),
    path('register/code/' , views.verify, name='code_view'),
    path('api/reservations/' ,views.reservation_api, name='reservation_api' ),
    path('register/code/calendar/', views.calendar, name='calendar'),
    path('register/code/calendar/welcome/' ,views.welcome, name='welcome'),

]
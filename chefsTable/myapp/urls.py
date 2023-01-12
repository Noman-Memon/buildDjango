from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hello/', views.hello, name="hello"),
    path('dateTime/', views.dateTime, name="date-Time"),
    path('menu/', views.menu, name="menu"),
    path('about/', views.about, name="about"),
    path('fruits/<str:name>', views.menueItem, name='menueItem'),
    path('form/', views.form, name='form'),
    path('form_view/', views.form_view, name='form_view'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    
    
]
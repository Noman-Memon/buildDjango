from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hello/', views.hello, name="hello"),
    path('dateTime/', views.dateTime, name="date-Time"),
    path('menue/', views.menue, name="menue"),
    path('fruits/<str:name>', views.menueItem, name='menueItem'),
    path('form/', views.form, name='form'),
    path('form_view/', views.form_view, name='form_view'),
]
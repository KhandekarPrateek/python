from django.urls import path
from . import views

#we import what we need to show here using views and any function in it and give the url path also 
urlpatterns=[
    path('',views.index,name='index'),
    path('counter',views.counter,name='counter')
]
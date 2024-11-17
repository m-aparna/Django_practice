from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('hello_world/', views.hello, name='hello_world'),
    path('hello_world/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'), 
]
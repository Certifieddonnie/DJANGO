from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('index/', views.index, name='main-view'),
    path('add', views.add, name="add")
]

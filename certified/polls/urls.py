from django.urls import path
from . import views

urlpatterns = [
    # path('indes', views.blah, name="blah"),
    path('indes', views.index, name='index'),
    path('home', views.home, name="home"),
    path('home2', views.home2, name="home2"),
    path('checker', views.checker, name="checker"),
    path('check', views.check, name="check"),
    path('add', views.add, name="add"),
    path('sub', views.sub, name="sub")
]

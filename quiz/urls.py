from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('play/' , views.play , name='play'),
    path('category',views.category, name='category'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('play/', views.play_game, name='play'),
]

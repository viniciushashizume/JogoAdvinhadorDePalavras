from django.urls import path
from . import views

urlpatterns = [
    path('', views.jogo_view, name='jogo'),
]
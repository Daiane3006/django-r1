from django.urls import path
from recipes.views import home, receita, sobre, contato

urlpatterns = [
    path('home/', home, name="home"),
    path('receita/', receita, name="receita"),
    path('sobre/', sobre),
    path('contato/', contato),
]
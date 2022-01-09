from django.urls import path

from anime.views import anime_search, anime_detailed

urlpatterns = [
    path('', anime_search, name='index'),
    path('<str:pk>', anime_detailed, name='anime-detail')
]

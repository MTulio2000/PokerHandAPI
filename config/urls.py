from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from player.views import PlayerViewSet
from game.views import GameViewSet

#players router
players = routers.DefaultRouter()
players.register(r'players',PlayerViewSet)

#game router
game = routers.DefaultRouter()
game.register(r'games',GameViewSet)

#url to acces each query
urlpatterns = [
    path('admin/', admin.site.urls),
    path('players/',include(players.urls)),
    path('games/',include(game.urls)),
]

from rest_framework import viewsets
from game.models import Game
from game.serializer import GameSerializer

#in this way, the rest_framework implement the CRUD
class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


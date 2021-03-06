from game.utils.round import Round
from django.db import models
from player.models import Player
from game.utils.hand import Hand

MAX_PLAYERS = 10
INITIAL_CHIPS = 4300

#game table
class Game(models.Model):
     players = [(Player,float,Hand)]
     deck, round,hidden = [],[Round],[]

     name = models.CharField(max_length=15)
     havePass = models.BooleanField(default=False)
     password = models.CharField(max_length=50)
         
     def __str__(self) -> str:
         return self.name

__all__ = [
    'Game',
    'MAX_PLAYERS',
    'INITIAL_CHIPS'
]
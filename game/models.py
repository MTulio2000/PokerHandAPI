from django.db import models
from player.models import Player

MAX_PLAYERS = 10
INITIAL_CHIPS = 4300

class Game(models.Model):
     players = []

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
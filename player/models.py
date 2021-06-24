from django.db import models
from hand.models import Hand

class Player(models.Model):
    name = models.CharField(max_length=10)

    def setHand(self, cards : str) -> None:
        self.hand = Hand(cards)

    def __str__(self) -> str:
        return self.name
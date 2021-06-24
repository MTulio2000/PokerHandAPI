from django.db import models
from card.models import Card

class Hand(models.Model):
    cards = []
    handType = 0

    def __init__(self,cards : str) -> None:
        super.__init__()
        for card in cards.split():
            self.cards.append(Card(card))
        self.cards.sort()

    def setType(self,value : int) -> None:
        self.handType = value
      

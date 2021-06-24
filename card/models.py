from django.db import models

class Card(models.Model):
    number = -1
    suit = "0"
    def __init__(self, card : str) -> None:
        number = ord(card[0])
        suit = card[1]

    def __gt__(self,other):
        return self.number>other.number

    def __lt__(self,other):
        return self.number<other.number
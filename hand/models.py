from django.db import models

class Hand(models.Model):
    cards = []
    handType = 0

    def __init__(self,str : str) -> None:
        super.__init__()
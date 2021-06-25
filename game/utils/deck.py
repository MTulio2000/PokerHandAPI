from game.utils.number import *
from game.utils.suits import *
from game.utils.card import Card
from itertools import product

deck = []

import itertools
for i, j in product(kinds,suits):
    deck.append(Card(convertNumber(i)+convertSuit(j)))

__all__ = [
    'deck'
]
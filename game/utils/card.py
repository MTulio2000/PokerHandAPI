from game.utils.number import *
from game.utils.suits import *

class Card(object):

    def __init__(self, card : str) -> None:
        self.number = convertNumber(card[0])
        self.suit = convertSuit(card[1])
        self.card = card

    def __gt__(self,other):
        return self.number>other.number

    def __lt__(self,other):
        return self.number<other.number

    def __eq__(self,other):
        return self.number==other.number

    def __str__(self) -> str:
        return self.card

__all__ = [
    'Card',
    'kinds',
    'TWO',
    'THREE',
    'FOUR',
    'FIVE',
    'SIX',
    'EIGHT',
    'NINE',
    'TEN',
    'JOKER',
    'QUEEN',
    'KING',
    'ACE',
    'suits',
    'CLUBS',
    'SPADES',
    'HEARTHS',
    'DIAMONDS',
]
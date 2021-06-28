from game.utils.card import Card
from game.strategies.context import Context
from game.strategies.royalflush import evaluate as royalflush
from game.strategies.straightflush import evaluate as straightflush
from game.strategies.four import evaluate as four
from game.strategies.fullhouse import evaluate as fullhouse
from game.strategies.flush import evaluate as flush
from game.strategies.straight import evaluate as straight
from game.strategies.three import evaluate as three
from game.strategies.twopair import evaluate as two
from game.strategies.onepair import evaluate as one

HIGH_CARD = 0
ONE_PAIR = 1
TWO_PAIR = 2
THREE_OF_A_KIND = 3
STRAIGHT = 4
FLUSH = 5
FULL_HOUSE = 6
FOUR_OF_A_KIND = 7
STRAIGHT_FLUSH = 8
ROYAL_FLUSH = 9

evaluate = [
    (royalflush,ROYAL_FLUSH),
    (straightflush,STRAIGHT_FLUSH),
    (four,FOUR_OF_A_KIND),
    (fullhouse,FULL_HOUSE),
    (flush,FLUSH),
    (straight,STRAIGHT),
    (three,THREE_OF_A_KIND),
    (two,TWO_PAIR),
    (one,ONE_PAIR),
]

class Hand(object):
    def __init__(self):
        self.cards = []
        self.context = Context()
        self.value = HIGH_CARD

    def add_card(self, card: Card):
        self.cards.append(card)
        self.cards.sort()

    def evaluate(self):
        for value in evaluate:
            self.context.setStrategy(value[0])
            if self.context.execute():
                self.value = value[1]
                break
    
__all__ = [
    'HIGH_CARD',
    'ONE_PAIR',
    'TWO_PAIR',
    'THREE_OF_A_KIND',
    'STRAIGHT',
    'FLUSH',
    'FULL_HOUSE',
    'FOUR_OF_A_KIND',
    'STRAIGHT_FLUSH',
    'ROYAL_FLUSH',
    'Hand'
]
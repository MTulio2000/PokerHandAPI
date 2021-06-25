from game.card import *
from game.utils.samesuit import samesuit
from game.utils.sequence import sequence

def evaluate(cards : list(Card))-> bool :
    same = samesuit(cards)
    seq = sequence(cards)
    return not seq and same
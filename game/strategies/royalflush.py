from game.card import *
from game.utils.samesuit import samesuit
from game.utils.sequence import sequence

def evaluate(cards : list(Card))-> bool :
    same = samesuit(cards)
    seq = sequence(cards)
    haveKing = KING in cards
    haveAce = ACE in cards
    return seq and same and haveKing and haveAce
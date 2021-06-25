from game.utils.samesuit import samesuit
from game.utils.sequence import sequence

def evaluate(cards)-> bool :
    same = samesuit(cards)
    seq = sequence(cards)
    return seq and same
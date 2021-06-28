from game.utils.samesuit import samesuit
from game.utils.sequence import sequence
from game.hand import ACE
from game.strategies.highcard import draw as highDraw

def evaluate(cards)-> bool :
    same = samesuit(cards)
    seq = sequence(cards)
    return seq and not same

def draw(hands):
    for i in 2:
        hands[i].remove(ACE)
    return highDraw(hands)

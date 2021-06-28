from game.utils.card import *
from game.utils.handcounter import *
from game.utils.major import drawMajor

def evaluate(cards)-> bool :
    return count(cards,4)


def draw(hands) -> int :
    value = lambda x,hands: hands[x].index(4) >  hands[(x+1)%2].index(4)
    return drawMajor(hands,value)
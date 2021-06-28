from game.utils.handcounter import *
from game.utils.major import major,drawMajor

def evaluate(cards)-> bool :
    return count(cards,2,1)

def draw(hands):
    value = lambda x: major(x,2)>major(((x+1)%2,2))
    return drawMajor(hands,value)
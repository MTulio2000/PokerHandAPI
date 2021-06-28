from game.utils.handcounter import *
from game.utils.major import major,drawMajor

def evaluate(cards)-> bool :
    return count(cards,3)

def draw(hands) -> int :
    value = lambda x: major(x,3)>major(((x+1)%2,3))
    return drawMajor(hands,value)
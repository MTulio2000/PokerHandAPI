from game.utils.handcounter import *
from game.utils.major import major,drawMajor

def evaluate(cards)-> bool :
    return count(cards,2,2)

def draw(hands):
    result = -1
    value = lambda x: major(x,2)>major(((x+1)%2,2))
    def clear(i):
        hands.counter[major(i,2)] = 0
    while result == -1:
        result = drawMajor(hands,value)
        if result == -1:
            for i in range(2):
                clear(i)
            
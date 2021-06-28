from game.utils.samesuit import samesuit
from game.utils.sequence import sequence
from game.utils.card import *

def evaluate(cards)-> bool :
    same = samesuit(cards)
    seq = sequence(cards)
    return not seq and same

def draw(hands) -> int:
    less = lambda x:1 if hands[x][4] == ACE else 0
    winner = lambda x,i: hands[x][i-less(x)]>hands[(x+1)%2][i-less((x+1)%2)] 
    for i in range(4,-1,-1):
        for j in range(2):
            if winner(j,i):
                return i
    return -1
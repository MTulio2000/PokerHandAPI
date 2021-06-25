from game.card import *

def sequence(cards : list(Card))-> bool :
    same = [0,0,0,0]
    for i in range(len(cards)-1):
        if cards[i].number < cards[i+1].number-1:
            return False
    return True

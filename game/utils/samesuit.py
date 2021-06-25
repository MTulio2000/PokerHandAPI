from game.utils.card import *

def samesuit(cards)-> bool :
    same = [0,0,0,0]
    for card in cards:
        same[card.suit]+=1
    for i in same:
        if i >= 5:
            return True
    return False

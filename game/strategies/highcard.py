from game.utils.handcounter import *

def draw(hands):
    size = min(len(hands[0].cards),len(hands[1].cards))
    for i in range(size,-1,-1):
        for j in range(2):
            if hands[j][i]>hands[j][(i+1)%2]:
                return j
    return -1
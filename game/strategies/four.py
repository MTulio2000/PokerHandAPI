from game.card import *
from game.utils.handcounter import *

def evaluate(cards : list(Card))-> bool :
    return count(cards,4)
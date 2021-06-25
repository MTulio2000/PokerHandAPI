from game.card import *
from game.strategies.onepair import evaluate as one
from game.strategies.three import evaluate as three

def evaluate(cards : list(Card))-> bool :
    return three(cards) and one(cards)
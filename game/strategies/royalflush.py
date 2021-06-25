from game.utils.card import *
from game.strategies.straightflush import evaluate as straightflush

def evaluate(cards)-> bool :
    haveKing = KING in cards
    haveAce = ACE in cards
    return straightflush(cards) and haveKing and haveAce
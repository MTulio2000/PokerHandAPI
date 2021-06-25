from game.utils.card import *
from game.utils.number import *

def count(cards)-> list :
    counter = []
    for kind in kinds:
        counter.append(cards.count(kind))
    return counter

def count(cards, n : int) -> int:
    return count(cards).count(n)

def count(cards, n : int, total : int) -> bool:
    return count(cards,n) == total

__all__ = [
    'count'
]
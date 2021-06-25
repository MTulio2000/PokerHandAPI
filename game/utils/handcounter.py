from game.card import *

def count(cards : list(Card))-> list :
    counter = []
    for kind in kinds:
        counter.append(cards.count(kind))
    return counter

def count(cards : list(Card), n : int) -> int:
    return count(cards).count(n)

def count(cards : list(Card), n : int, total : int) -> bool:
    return count(cards,n) == total

__all__ = [
    'count'
]
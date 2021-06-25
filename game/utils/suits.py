
CLUBS = 0
SPADES = 1
HEARTHS = 2
DIAMONDS = 3

suits = [
    CLUBS,
    SPADES,
    HEARTHS,
    DIAMONDS
]


def strToSuit(suit : str) -> int:
    if suit == 'S':
        return SPADES
    if suit == 'H':
        return HEARTHS
    if suit == 'C':
        return CLUBS
    if suit == 'D':
        return DIAMONDS
    return -1


def suitToStr(suit : int) -> int:
    if suit == SPADES:
        return 'S'
    if suit == HEARTHS:
        return 'H'
    if suit == CLUBS:
        return 'C'
    if suit == DIAMONDS:
        return 'D'
    return ""

def convertSuit(str : str) -> int:
    return strToSuit(str)
def convertSuit(suit : int) -> str:
    return suitToStr(suit)

__all__ = [
    'suits',
    'CLUBS',
    'SPADES',
    'HEARTHS',
    'DIAMONDS',
    'convertSuit'
]
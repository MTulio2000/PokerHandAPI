TWO = 0
THREE = 1
FOUR = 2
FIVE = 3
SIX = 4
EIGHT = 5
NINE = 6
TEN = 7
JOKER = 8
QUEEN = 9
KING = 10
ACE = 11

kinds = [
    TWO,
    THREE,
    FOUR,
    FIVE,
    SIX,
    EIGHT,
    NINE,
    TEN,
    JOKER,
    QUEEN,
    KING,
    ACE
]
def strToNumber(number : str) -> int:
    value = ord(number)-50
    if value < 7: 
        return value
    if number == 'T':
        return TEN
    if number == 'J':
        return JOKER
    if number == 'Q':
        return QUEEN
    if number == 'K':
        return KING
    if number == 'A':
        return ACE

def numberToStr(value : int) -> str:
    if value < 7: 
        return chr(value+50)
    if value == TEN:
        return 'T'
    if value == JOKER:
        return 'J'
    if value == QUEEN:
        return 'Q'
    if value == KING:
        return 'K'
    if value == ACE:
        return 'A'

def convertNumber(str :str) -> int:
    return strToNumber(str)
    
def convertNumber(value :int) -> str:
    return strToNumber(value)

__all__ = [
    'TWO',
    'THREE',
    'FOUR',
    'FIVE',
    'SIX',
    'EIGHT',
    'NINE',
    'TEN',
    'JOKER',
    'QUEEN',
    'KING',
    'ACE',
    'kinds',
    'convertNumber'
]
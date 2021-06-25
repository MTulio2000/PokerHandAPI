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

CLUBS = 0
SPADES = 1
HEARTHS = 2
DIAMONDS = 3

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

def convertNumber(number : str) -> int:
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

def convertSuit(suit : str) -> int:
    if suit == 'S':
        return SPADES
    if suit == 'H':
        return HEARTHS
    if suit == 'C':
        return CLUBS
    if suit == 'D':
        return DIAMONDS
    return -1

class Card(object):

    def __init__(self, card : str) -> None:
        self.number = convertNumber(card[0])
        self.suit = convertSuit(card[1])
        self.card = card

    def __gt__(self,other):
        return self.number>other.number

    def __lt__(self,other):
        return self.number<other.number

    def __eq__(self,other):
        return self.number==other.number

    def __str__(self) -> str:
        return self.card

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
    'Card',
    'CLUBS',
    'SPADES',
    'HEARTHS',
    'DIAMONDS',
    'kinds'
]
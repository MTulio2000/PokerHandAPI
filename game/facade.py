from game.utils.number import FOUR
from game.models import *
from player.models import Player
import random
from game.utils.deck import deck
from game.utils.hand import *
from itertools import product
from game.strategies.four import draw as fourDraw
from game.strategies.flush import draw as flushDraw
from game.strategies.onepair import draw as oneDraw
from game.strategies.three import draw as threeDraw
from game.strategies.twopair import draw as twoDraw
from game.strategies.highcard import draw as highDraw
from game.strategies.straight import draw as straightDraw
from game.utils.round import Round

#add a plaeyr in a game
def addPlayer(game : Game, player : Player, password : str) -> bool:
    max_player = len(game.players)<MAX_PLAYERS-1
    if not game.havePass or password == game.password and max_player:
        game.players[str(player._id)] = ((player,INITIAL_CHIPS,Hand()))
        return True
    return False

#remove a player from the game
def removePlayer(game : Game, player : Player, password : str) -> bool:
    if game.players[str(player._id)]:
        game.players.pop(str(player._id))
        return True
    return False

#deal the cards for all players and the hidden cards
def deal(game : Game) -> None:
    for i, in product(len(game.players),2):
        card = random.randint(0,len(game.deck)-1)
        game.players[i][2].add_card(game.deck[card])
        game.deck.remove(card)
    for _ in range(3):
        card = random.randint(0,len(game.deck)-1)
        game.hidden.append(game.deck[card])
        game.deck.remove(card)

#initial configuration for the game
def initialize_game(game : Game) -> None:
    game.deck = random.sample(deck)
    deal(game)

#flip a card from the hidden deck of the game
def flip_card(game : Game) -> bool:
    if len(game.hidden):
        card = game.hidden[0]
        game.hidden.remove(0)
        for i in range(len(game.players)):
            game.players[i][2].add_card(card)
        return True
    return False

#draw object to help to verify the draw case
draw = {
    FOUR_OF_A_KIND : fourDraw,
    FLUSH : flushDraw,
    ONE_PAIR : oneDraw,
    TWO_PAIR : twoDraw,
    THREE_OF_A_KIND : threeDraw,
    FULL_HOUSE : threeDraw,
    HIGH_CARD : highDraw,
    STRAIGHT : straightDraw,
    STRAIGHT_FLUSH : straightDraw
}

#verify the winner
def check_winner(game : Game) -> int:
    best = 0
    index = -1
    def setWinner(i):
        return i,game.players[i][2].value
    def verifyWinner(i):
        hand1 = game.players[index][2]
        hand2 = game.players[i][2]
        type_hand = game.players[i][2].value
        return draw[type_hand]([hand1,hand2]) == 1

    def verifyMajor(i):
        return best < game.players[i][2].value

    for i in range(len(game.players)):
        game.players[i][2].evaluate()
        if game.players[i][2].value == best:
            if verifyWinner(i) or verifyMajor(i):
                index,best = setWinner(i)
    return index
    
#start a new round
def newRound(game : Game):
    game.round.append(Round())

#set player action in the current round
def setRoundPlayer(game : Game, player : Player, action : int, value = 0) -> bool:
    size = len(game.round)-1
    return size >= 0 and game.round[size].addPlayer(player,action,value)

__all__ = [
    'remove_player',
    'addPlayer',
    'initialize_game',
    'flip_card',
    'check_winner',
    'setRoundPlayer',
    'newRound',
]
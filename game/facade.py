from game.models import *
from player.models import Player
import random
from game.utils.deck import deck
from game.hand import Hand
from itertools import product

def addPlayer(game : Game, player : Player, password : str) -> bool:
    max_player = len(game.players)<MAX_PLAYERS-1
    if not game.havePass or password == game.password and max_player:
        game.players[str(player._id)] = ((player,INITIAL_CHIPS,Hand()))
        return True
    return False

def removePlayer(game : Game, player : Player, password : str) -> bool:
    if game.players[str(player._id)]:
        game.players.pop(str(player._id))
        return True
    return False

def player_bet(game : Game, player : Player, value : float) -> bool:
    if game.players[str(player._id)][1] >= value:
        game.players[str(player._id)][1]-=value
        return True
    return False


def deal(game : Game) -> None:
    for i, in product(len(game.players),2):
        card = random.randint(0,len(game.deck)-1)
        game.players[i][2].add_card(game.deck[card])
        game.deck.remove(card)
    for _ in range(3):
        card = random.randint(0,len(game.deck)-1)
        game.hidden.append(game.deck[card])
        game.deck.remove(card)

def initialize_game(game : Game) -> None:
    game.deck = random.sample(deck)
    deal(game)

def flip_card(game : Game) -> bool:
    if len(game.hidden):
        card = game.hidden[0]
        game.hidden.remove(0)
        for i in range(len(game.players)):
            game.players[i][2].add_card(card)
        return True
    return False

def check_winner(game : Game) -> int:
    for i in range(len(game.players)):
        game.players[i][2].evaluate()
    index = -1
    return index
    

__all__ = [
    'player_bet',
    'remove_player',
    'addPlayer',
    'initialize_game',
    'flip_card',
    'check_winner'
]
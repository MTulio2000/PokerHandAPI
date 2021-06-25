from game.models import *
from player.models import Player

def addPlayer(game : Game, player : Player, password : str) -> bool:
    max_player = len(game.players)<MAX_PLAYERS-1
    if not game.havePass or password == game.password and max_player:
        game.players[str(player._id)] = ((player,INITIAL_CHIPS))
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

__all__ = [
    'player_bet',
    'remove_player',
    'addPlayer'
]
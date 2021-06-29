from player.models import Player
from game.utils.hand import Hand

__all__ = [
    'set_hand'
]

#set the hand for the player in the current game
def set_hand(player : Player, hand:Hand) -> bool:
    player.hand = hand

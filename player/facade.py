from player.models import Player

__all__ = [
    'create_player'
]

def create_player(name : str, hand : Hand) -> bool:
    return Player.objects.create(name,hand)

def set_hand(player : Player, hand:Hand) -> bool:
    player.hand = hand
    player.save()

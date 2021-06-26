from player.models import Player

CHECK = 0
BET = 1
CALL = 2
RAISE = 3
PASS = 4
FOLD = 5

INITIAL = 0
FINAL = 1

possible_actions = {
    INITIAL : [BET,CHECK],
    FINAL : [FOLD,RAISE,CALL]
}

class Round():
    def __init__(self):
        self.value = 0
        self.players = []
        self.state = INITIAL
        self.major = 0

    def addPlayer(self,player : Player, action : int,value = 0.0) -> None:
        if possible_actions[self.state].count(action) and value >= self.major:
            self.players.append(player)
            self.value += value

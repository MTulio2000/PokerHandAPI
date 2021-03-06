from player.models import Player

CHECK = 0
BET = 1
CALL = 2
RAISE = 3
PASS = 4
FOLD = 5

INITIAL = 0
FINAL = 1

#possible actions for each state
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

    #add a player round
    def addPlayer(self,player : Player, action : int,value = 0.0) -> bool:
        if possible_actions[self.state].count(action) and value >= self.major:
            self.players.append(player)
            self.value += value
            if action >= 1:
                self.state = FINAL
            return True
        return False

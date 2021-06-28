 #return the index of the major pair/three/four kinds
# def index(hand,n:int,less:int):
#     index = -1
#     for i in range(0,len(hand.equals)-less):
#         if hand.equals[i][0] == n:
#             index = hand.equals[i][2]
#     return index

# def winner(hands,n):
#     less = 0
#     while True:
#         mineIndex = index(self.hand,n,less)
#         adversaryIndex = index(hand,n,less)
#         if self.hand.hand[mineIndex]>advHand[adversaryIndex]:
#             return Result.WIN
#         elif self.hand.hand[mineIndex]<advHand[adversaryIndex]:
#             return Result.LOSS
#         else:
#             if less == 2:
#                 break
#             less+=1
#     return -1

def major(n,hand) -> int:
     return len(hand.counter) - 1 - hand.counter[::-1].index(n)

def drawMajor(hand,f) -> int:
    for i in range(2):
        if f(i,hand):
            return i
    return -1
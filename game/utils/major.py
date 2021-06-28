def major(n,hand) -> int:
     return len(hand.counter) - 1 - hand.counter[::-1].index(n)

def drawMajor(hand,f) -> int:
    for i in range(2):
        if f(i,hand):
            return i
    return -1
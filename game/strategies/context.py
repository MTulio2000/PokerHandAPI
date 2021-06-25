
class Context():
    def __init__(self):
        self.__strategy = -1

    def setStrategy(self,strategy):
        self.__strategy = strategy

    def execute(self):
        return self.__strategy()
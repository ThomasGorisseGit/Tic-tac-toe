from abc import abstractmethod
from Models.Playable import Playable

class Bot(Playable):
    def __init__(self, playerName, symbol):
        super().__init__(playerName, symbol)


    @abstractmethod
    def makeChoice(self, grid):
        return 0, 0

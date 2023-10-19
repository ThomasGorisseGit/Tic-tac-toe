from abc import ABC, abstractmethod


class Playable(ABC):
    def __init__(self, playerName,symbol):
        self.name = playerName
        self.symbol = symbol

    @abstractmethod
    def makeChoice(self, grid, firstPlayer):
        return 0, 0

from abc import ABC, abstractmethod


class Playable(ABC):
    def __init__(self, playerName,symbol):
        self.name = playerName
        self.symbol = symbol

    @abstractmethod
    def makeChoice(self, grid):
        return 0, 0

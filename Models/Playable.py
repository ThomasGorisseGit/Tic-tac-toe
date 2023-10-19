from abc import ABC, abstractmethod


class Playable(ABC):
    def __init__(self, playerName):
        self.name = playerName

    @abstractmethod
    def makeChoice(self):
        return 0, 0

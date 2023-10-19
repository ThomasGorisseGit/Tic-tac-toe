from abc import ABC, abstractmethod
from Models.Playable import Playable


class Bot(ABC, Playable):
    """
    Abstract class
    Bot model
    """

    def __init__(self, name="BOT"):
        Playable.__init__(self, name)

    @abstractmethod
    def makeChoice(self):
        """
        Allows Bots to make a choice
        :return:
        """
        pass

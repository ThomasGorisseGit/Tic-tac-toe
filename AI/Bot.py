from abc import ABC, abstractmethod


class Bot(ABC):
    """
    Abstract class
    Bot model
    """
    def __init__(self,nom):
        self.name = nom

    @abstractmethod
    def makeChoice(self):
        """
        Allows Bots to make a choice
        :return:
        """
        pass


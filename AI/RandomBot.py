import random
from Models.Bot import Bot

class RandomBot(Bot):
    def __init__(self, symbol, botName="RandomBot"):
        Bot.__init__(self, botName,symbol)

    def makeChoice(self, firstPlayer, grid=None):
        i = random.randint(0, 2)
        j = random.randint(0, 2)
        return i, j



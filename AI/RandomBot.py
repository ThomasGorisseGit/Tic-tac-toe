import random
from Models.Playable import Playable

class RandomBot(Playable):
    def __init__(self, botName="RandomBot"):
        Playable.__init__(self, botName)

    def makeChoice(self):
        i = random.randint(0, 2)
        j = random.randint(0, 2)
        return i, j


if __name__ == '__main__':
    myBot = RandomBot("Joe")
    print(myBot.name)
    print(myBot.makeChoice())

import random
from Bot import Bot


class RandomBot(Bot):
    def __init__(self, botName="RandomBot"):
        Bot.__init__(self, botName)

    def makeChoice(self):
        i = random.randint(0, 2)
        j = random.randint(0, 2)
        return i, j


if __name__ == '__main__':
    myBot = RandomBot("Joe")
    print(myBot.name)
    print(myBot.makeChoice())

import random

from Models import Grid
from Views import Prompt


class Game():
    def __init__(self):
        self.view = Prompt.Prompt(self)
        self.grid = Grid.Grid()
        self.player1 = ""
        self.player2 = ""
        self.whoToPlay = ""
        self.state = 1
        self.runGame()

    def getRandomStart(self):
        if random.randint(0, 1) == 1:
            self.whoToPlay = self.player1
        else:
            self.whoToPlay = self.player2

    def changeTurn(self):
        if self.whoToPlay == self.player1:
            self.whoToPlay = self.player2
        else:
            self.whoToPlay = self.player1

    def getValueToSet(self):
        if self.whoToPlay == self.player1:
            return 'x'
        else:
            return 'o'

    def getPlayerFromValue(self, value):
        if value == 'x':
            return self.player1
        return self.player2

    def runGame(self):
        while True:
            match self.state:
                case 1:
                    self.player1 = self.view.getUserNames("1")
                    self.player2 = self.view.getUserNames("2")
                    self.state += 1
                case 2:
                    self.grid.resetGrid()
                    self.getRandomStart()
                    self.state += 1
                case 3:
                    while self.grid.getWinner() == ' ':
                        self.view.displayTurn(self.whoToPlay)
                        getUserRowInput = self.view.getUserInputs("row")
                        getUserColumnInput = self.view.getUserInputs("column")
                        self.grid.setValue(getUserColumnInput, getUserRowInput, self.getValueToSet())
                        self.grid.displayGrid()
                        self.changeTurn()
                    self.view.displayWinner(self.getPlayerFromValue(self.grid.getWinner()) + " (" + self.grid.getWinner() + ")")
                    self.view.handleEnding()

if __name__ == '__main__':
    game = Game()

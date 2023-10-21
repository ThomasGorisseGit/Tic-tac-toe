import random

from Models.Grid import Grid
from Views.GameView import Prompt


class Game():
    """
        In MVC Architecture the controller is the leader of the program,
        It uses the data from the models to play the game
        and call the views to display the game.

        It is very useful when you have multiple view, or when a lot of coworkers works on the program.
        It is very easy to decompose the program.

        Game is the entry point, the launcher must instantiate this class to start the game.
    """

    def __init__(self):
        """
        view : Display the information
        grid : Model (data of the game)
        player1 / player2 : Players
        whoToPlay : The current player who has to play
        state : The game state -> used to handle the end (restart, continue, quit)
        runGame : start a game
        """
        self.grid = Grid()
        self.player1 = None
        self.player2 = None
        self.whoToPlay = None
    def setPlayers(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def getRandomStart(self):
        """
            Define randomly who of the two players plays first.
        """
        if random.randint(0, 1) == 1:
            self.whoToPlay = self.player1
        else:
            self.whoToPlay = self.player2

    def changeTurn(self):
        """
        Change the player who has to play. It is call at the end of each Round
        :return:
        """
        if self.whoToPlay == self.player1:
            self.whoToPlay = self.player2
        else:
            self.whoToPlay = self.player1

    def getValueToSet(self):
        """
        To each player, we attribute a symbol
        Player1 -> 'x'
        Player2 -> 'o'

        :return: Either 'x' or 'o' (the symbol of the current player)
        """
        if self.whoToPlay == self.player1:
            return 'x'
        else:
            return 'o'

    def getPlayerFromValue(self, symbol):
        """
        We return the player name with the symbol

        :param symbol: Either 'x' or 'o'
        :return: Player name
        """
        if symbol == 'x':
            return self.player1
        return self.player2

    def resetGrid(self):
        self.grid.resetGrid()

    def getScore(self):
        return self.grid.getScore()
    def makePlayerPlay(self):
        return self.whoToPlay.makeChoice(self.grid)

    def tryToSetValues(self, values):
        print(values)
        return self.grid.setValue(values[1], values[0], self.whoToPlay.symbol)
    def getGrid(self):
        return self.grid.getGrid()
    def getWinner(self):
        return self.grid.getWinner()
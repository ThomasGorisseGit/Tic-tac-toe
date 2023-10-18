import random

from Models import Grid
from Views import Prompt


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
        self.view = Prompt.Prompt(self)
        self.grid = Grid.Grid()
        self.player1 = ""
        self.player2 = ""
        self.whoToPlay = ""
        self.state = 1
        self.runGame()

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

    def runGame(self):
        """
        The main method :
        It is the game execution divided in 4 states

        case 1 : We retrieve players names from the view. In MVC Architecture, the View is the only component
        responsible for the communication with the users

        case 2 : The game started, we determine who is starting to play

        case 3 : It is a while on a Round  :
                We get user inputs, and we fill the grid
                until there is a winner

        case 4 : Handle the end of the game : Restart, Continue, Quit

        :return: None
        """
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
                    self.state += 1
                case 4:
                    self.view.displayWinner(self.getPlayerFromValue(self.grid.getWinner()) + " (" + self.grid.getWinner() + ")")
                    self.view.handleEnding()



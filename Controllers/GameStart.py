from Views.GameView import Prompt
from Models.Game import Game
from Controllers.Player import Player
from AI.RandomBot import RandomBot
from AI.MinimaxBot import MinimaxBot

class GameStart():
    def __init__(self):
        self.view = Prompt(self)
        self.game = Game()
        self.state = "Beginning"

        self.runGame()

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
                case "Beginning":
                    self.view.choosePlayers()

                case "PvP":
                    player1 = Player('x')
                    player2 = Player('o')
                    self.game.setPlayers(player1, player2)

                    self.state = "InitGrid"

                case "PvB":
                    player1 = Player('x')
                    bot1 = MinimaxBot('o')
                    self.game.setPlayers(player1, bot1)
                    self.state = "InitGrid"

                case "BvB":
                    bot1 = RandomBot("x","RandomBot 1 - Fry")
                    bot2 = MinimaxBot("o", "MiniMax 2 - John")
                    self.game.setPlayers(bot1, bot2)
                    self.state = "InitGrid"

                case "InitGrid":
                    self.game.resetGrid()
                    self.game.getRandomStart()
                    self.state = "Game"
                case "Game":
                    while self.game.getScore() == ' ':
                        self.view.displayTurn(self.game.whoToPlay)

                        isValueAccepted = False
                        while isValueAccepted != True:
                            """
                            isValueAccepted == 0 if the value is accepted  
                            if the value is different, display the result   
                            """
                            playerInputs = self.game.makePlayerPlay()
                            isValueAccepted = self.game.tryToSetValues(playerInputs)
                            if not isValueAccepted:
                                self.view.displayException(isValueAccepted)

                        self.view.displayGrid(self.game.getGrid())
                        self.game.changeTurn()
                    self.state = "HandleEnding"
                case "HandleEnding":
                    if self.game.getScore() == 'tie':
                        self.view.displayDraw()
                    else:
                        self.view.displayWinner(
                            self.game.getPlayerFromValue(
                                self.game.getWinner()).name + " (" + self.game.getWinner() + ")")
                    self.view.handleEnding()

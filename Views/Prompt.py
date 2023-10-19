class Prompt:
    """
    In MVC Architecture, the View is the link between the program and the users
    It is used to display content and retrieve user inputs
    """
    def __init__(self, controller):
        """
        Construct the view
        :param controller: Give the controller to the view, in order to increase the state of the game after user action
        """
        self.controller = controller
    def displayTurn(self, player):
        """
        Display the player who has to play
        :param player: player name who has to play
        :return: None
        """
        print("--------------------------------------------------------")
        print("---------------ITS " + player + " TURN-------------------")
        print("--------------------------------------------------------")

    def getUserInputs(self, position):
        """
        Retrieve user choice
        :param position: the position either of the column or the row
        :return: the value of the user as an int
        """
        return int(input("Write " + position + " position "))

    def displayWinner(self, winner):
        """
        Display the winner of the game
        :param winner: player's name who wins the game
        :return: None
        """
        print("Winner : " + winner)

    def getUserNames(self, playerNumber):
        """
        Display the number of the player to insert
        :param playerNumber: int
        :return: player name (str)
        """
        return input("Enter the name of player " + playerNumber + " ")

    def handleEnding(self):
        """
        Switch case to handle the next state :
        continue -> We keep the names and a new game start
        restart -> We change the players
        Quit -> quit the program
        :return: None
        """
        response = input("To quit the game press Q,\nTo restart the game press R\nTo continue press Enter ")
        if response == 'q' or response == 'Q':
            exit()
        elif response == 'r' or response == 'R':
            self.controller.state = 1
        else:
            self.controller.state = 2

    def displayException(self, exceptionMessage):
        """
        Print exceptions
        :param exceptionMessage: display the exception message
        :return: None
        """
        print(exceptionMessage)
    def displayDraw(self):
        print("------------------------")
        print("----------DRAW----------")
        print("------------------------")

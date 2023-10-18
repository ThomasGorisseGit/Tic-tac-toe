class Prompt:
    def __init__(self, controller):
        self.controller = controller

    def displayInput(self, message):
        print(message)

    def displayTurn(self, player):
        print("--------------------------------------------------------")
        print("---------------ITS " + player + " TURN-------------------")
        print("--------------------------------------------------------")

    def getUserInputs(self, position):
        return int(input("Write " + position + " position "))

    def displayWinner(self, winner):
        print("Winner : " + winner)

    def getUserNames(self, playerNumber):
        return input("Enter the name of player " + playerNumber + " ")

    def handleEnding(self):
        response = input("To quit the game press Q,\nTo restart the game press R\nTo continue press Enter ")
        if response == 'q' or response == 'Q':
            exit()
        elif response == 'r' or response == 'R':
            self.controller.state = 1
        else:
            self.controller.state = 2

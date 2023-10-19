class PlayerView():
    def __init__(self, controller):
        self.controller = controller
    def getPlayerName(self):
        return input("Enter the player name ")

    def getInput(self,rowOrCol):
        return int(input("Enter the "+rowOrCol+" position : "))
    def getRowInput(self):
        return self.getInput("row")
    def getColumnInput(self):
        return self.getInput("column")

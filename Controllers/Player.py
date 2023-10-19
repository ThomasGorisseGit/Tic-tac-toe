from Models.Playable import Playable
from Views.PlayerView import PlayerView


class Player(Playable):

    def __init__(self, ):
        self.view = PlayerView(self)
        Playable.__init__(self, self.view.getPlayerName())

    def makeChoice(self):
        return self.view.getRowInput(), self.view.getColumnInput()

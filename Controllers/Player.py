from Models.Playable import Playable
from Views.PlayerView import PlayerView


class Player(Playable):

    def __init__(self, symbol):
        self.view = PlayerView(self)
        Playable.__init__(self, self.view.getPlayerName(), symbol)

    def makeChoice(self, grid=None):
        return self.view.getRowInput(), self.view.getColumnInput()

import copy
from math import inf
from Models.Grid import Grid

from Models.Bot import Bot


class MinimaxBot(Bot):
    def __init__(self, symbol, botName="MiniMaxBot"):
        Bot.__init__(self, botName, symbol)

    def makeChoice(self, newGrid, firstPlayer):
        isMaximizing = False
        if firstPlayer == self.symbol:
            isMaximizing = True
        grid = copy.deepcopy(newGrid)
        bestMove = (-1, -1)
        bestVal = -1000
        for i in range(3):
            for j in range(3):
                if grid.grid[i][j] == ' ':
                    grid.grid[i][j] = self.symbol

                    moveVal = self.minimax(grid, 0, isMaximizing)
                    grid.grid[i][j] = ' '
                    if moveVal > bestVal:
                        bestMove = (i, j)
                        bestVal = moveVal
        return bestMove

    def minimax(self, grid, depth, isMaximizingPlayer):
        score = grid.getScore()
        if score == self.symbol:
            return 10
        elif score == 'tie':
            return 0
        elif score != ' ':
            return -10
        if isMaximizingPlayer:
            best = -10000
            for i in range(3):
                for j in range(3):
                    if grid.grid[i][j] == ' ':
                        grid.grid[i][j] = self.symbol
                        chal = self.minimax(grid, depth + 1, not isMaximizingPlayer)
                        best = max(best, chal)
                        grid.grid[i][j] = ' '
            return best
        else:
            if (self.symbol == 'x'):
                opponent = 'o'
            else:
                opponent = 'x'
            best = 100000
            for i in range(3):
                for j in range(3):
                    if grid.grid[i][j] == ' ':
                        grid.grid[i][j] = opponent
                        chal = self.minimax(grid, depth + 1, not isMaximizingPlayer)
                        best = min(best,chal )
                        grid.grid[i][j] = ' '
            return best

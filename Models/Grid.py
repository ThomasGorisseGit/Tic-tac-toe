class Grid():
    """
    In MVC Architecture, the models are used to store the data of the application.

    In this case, Grid is used to recreate a Tic Tac Toe game

    """

    def __init__(self, add_grid=False):
        """
        Init a grid with nothing
        """
        self._firstRow = [' ', ' ', ' ']
        self._secondRow = [' ', ' ', ' ']
        self._thirdRow = [' ', ' ', ' ']
        self.grid = [self._firstRow, self._secondRow, self._thirdRow]
        if add_grid:
            self.grid = add_grid

    def setValue(self, column, row, symbol):
        """
        Set a value to a position and return 0 if the insertion had no issue
        :param column: position of column in the matrix
        :param row: position of row in the matrix
        :param symbol: symbol to insert
        :return: Either the error or a basic value
        """
        if symbol != 'x' and symbol != 'o':
            return "impossible value"
        if not (0 <= column < 3 and 0 <= row < 3):
            return "index out of range"

        if self.grid[row][column] != ' ':
            return "this box is not free"

        self.grid[row][column] = symbol
        return True

    def getGrid(self):
        gridFormat = '_____________ \n'
        for i in range(len(self.grid)):
            gridFormat += "| "
            for j in range(len(self.grid[i])):
                gridFormat += self.grid[i][j] + " | "
            gridFormat += "\n"
        return gridFormat

    def resetGrid(self):
        """
        Reinitialise the value thanks to the constructor
        :return:
        """
        self.__init__()

    def getWinner(self):
        """
        Find if a winner exist and return the symbol
        :return: Winner's symbol
        """
        winner = ' '
        for i in range(len(self.grid)):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] != ' ':
                winner = self.grid[i][0]
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] != ' ':
                winner = self.grid[0][i]

        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != ' ':
            winner = self.grid[0][0]

        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != ' ':
            winner = self.grid[0][2]

        return winner

    def getScore(self):
        winner = self.getWinner()
        if winner != ' ':
            return winner
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == ' ':
                    return ' '
        return 'tie'

    def possiblesMoves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if (self.grid[i][j] == ' '):
                    moves.append((i, j))
        return moves

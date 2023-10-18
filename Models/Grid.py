class Grid():
    """
    In MVC Architecture, the models are used to store the data of the application.

    In this case, Grid is used to recreate a Tic Tac Toe game

    """
    def __init__(self):
        """
        Init a grid with nothing
        """
        self._firstRow = [' ', ' ', ' ']
        self._secondRow = [' ', ' ', ' ']
        self._thirdRow = [' ', ' ', ' ']
        self.grid = [self._firstRow, self._secondRow, self._thirdRow]

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
        return 0
    def displayGrid(self):
        """
        Display the grid
        :return: None
        """
        print('_____________')
        for i in range(len(self.grid)):
            print("| ", end="")
            for j in range(len(self.grid[i])):
                print(self.grid[i][j] + " | ", end="")
            print("\n")

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

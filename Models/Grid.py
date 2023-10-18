class Grid():
    """
    In MVC Architecture, the models are used to store the data of the application.

    In this case, Grid is used to recreate a Tic Tac Toe game

    """
    def __init__(self):
        self._firstRow = [' ', ' ', ' ']
        self._secondRow = [' ', ' ', ' ']
        self._thirdRow = [' ', ' ', ' ']
        self.grid = [self._firstRow, self._secondRow, self._thirdRow]

    def setValue(self, column, row, value):
        if value != 'x' and value != 'o':
            raise Exception("Value must be either 'x' or 'o'")
        if not (0 <= column < 3 and 0 <= row < 3):
            if 0 <= column < 3:
                userInput = "Row input is"
            elif (0 <= row < 3):
                userInput = "Column input is"
            else:
                userInput = "Column and row inputs are"

            raise Exception(userInput + " out of grid | Must be between 0 and 2")

        if self.grid[row][column] != ' ':
            raise Exception("This box is already taken")

        self.grid[row][column] = value

    def displayGrid(self):
        print('_____________')
        for i in range(len(self.grid)):
            print("| ", end="")
            for j in range(len(self.grid[i])):
                print(self.grid[i][j] + " | ", end="")
            print("\n")

    def resetGrid(self):
        self.__init__()

    def getWinner(self):
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
if __name__ == '__main__':
    grid = Grid()

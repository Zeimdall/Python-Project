from boardbase import BoardBase


class Board(BoardBase):
    """ A board game with helpful methods.
    """
    def print(self):
        for i in range(self.n):
            print(self.board[i], end=" ")
            print()

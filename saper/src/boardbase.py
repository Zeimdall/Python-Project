import random

from src.cell import Cell, CellState


class BoardBase:
    """ A base board game with random generated bombs.
    """
    min_size = 2
    max_size = 15
    board = []

    def __init__(self, n, m, bomb_number):
        self.n = n
        self.m = m
        self.bomb_number = bomb_number
        self.total_set_as_bomb = 0

    '''
    Check of all parameters are valid, if not throws Exception
    '''

    def is_board_valid(self):
        if not BoardBase.min_size <= self.n <= BoardBase.max_size:
            raise Exception('N is not valid')
        elif not BoardBase.min_size <= self.m <= BoardBase.max_size:
            raise Exception('M is not valid')
        elif not 0 < self.bomb_number <= self.n * self.m:
            raise Exception('Number of bombs is not valid')

        return True

    '''
    Algorythm to check whether the board is won
    '''

    def is_board_win(self) -> bool:
        bombs_detected_correctly = 0
        for x in range(self.n):
            for y in range(self.m):
                cell = self.get_cell(x, y)
                if cell.is_state_sure_bomb() and cell.is_bomb:
                    bombs_detected_correctly += 1

        if bombs_detected_correctly == self.total_set_as_bomb == self.bomb_number:
            return True

        total_open = 0
        for x in range(self.n):
            for y in range(self.m):
                cell = self.get_cell(x, y)
                if cell.is_clicked() or cell.is_deactivated():
                    total_open += 1

        if self.n * self.m - total_open == self.bomb_number:
            return True

        return False

    def get_cell(self, x, y) -> Cell:
        return self.board[x][y]

    def click_cell(self, x, y):
        if self.get_cell(x, y).can_be_clicked():
            self.get_cell(x, y).set_state(CellState.CLICKED)
            self.deactivate_neighbours(x, y)

    def update_total_set_as_bomb(self):
        self.total_set_as_bomb = 0

        for x in range(self.n):
            for y in range(self.m):
                cell = self.get_cell(x, y)
                if cell.is_state_sure_bomb():
                    self.total_set_as_bomb += 1

    def create_board(self):
        if not self.is_board_valid():
            raise ValueError('Board is not valid.')

        self.board = dict()

        for i in range(self.n):
            self.board[i] = [Cell(i, j) for j in range(self.m)]

    '''
    Returns list of cells for cell by positions
    '''

    def get_neighbours_cells(self, x, y) -> [Cell]:
        cells = []
        neighbors = lambda _x, _y: [(x2, y2) for x2 in range(_x - 1, _x + 2)
                                    for y2 in range(_y - 1, _y + 2)
                                    if (-1 < _x < self.n and
                                        -1 < _y < self.m and
                                        (_x != x2 or _y != y2) and
                                        (0 <= x2 < self.n) and
                                        (0 <= y2 < self.m))]
        for neighbor in neighbors(x, y):
            cells.append(self.get_cell(neighbor[0], neighbor[1]))

        return cells

    '''
    After click on the cell, check whether neighbours cells can be deactivated (a.k.a. clicked)
    '''

    def deactivate_neighbours(self, x, y):
        can_neighbours_be_deactivated = True
        for cell in self.get_neighbours_cells(x, y):
            if cell.can_be_clicked() and cell.is_bomb:
                can_neighbours_be_deactivated = False
                break

        if can_neighbours_be_deactivated:
            for cell in self.get_neighbours_cells(x, y):
                if cell.can_be_clicked():
                    cell.set_state(CellState.DEACTIVATED)
                    self.deactivate_neighbours(cell.x, cell.y)

    def mark_cell(self, x, y):
        if not self.get_cell(x, y).is_clicked():
            self.get_cell(x, y).mark()

    def update_cell_values(self, x, y):
        cells = self.get_neighbours_cells(x, y)
        for cell in cells:
            cell.value += 1

    '''
    Added randomly bombs on the board
    '''

    def fill_up_bombs(self):
        for _ in range(self.bomb_number):
            while True:
                x = random.randint(0, self.n - 1)
                y = random.randint(0, self.m - 1)

                cell = self.get_cell(x, y)

                if not cell.is_bomb:
                    cell.set_bomb()
                    self.update_cell_values(x, y)
                    break

    @staticmethod
    def get_color(number_of_bombs):
        if number_of_bombs == 1:
            return 'blue'
        elif number_of_bombs == 2:
            return 'green'
        elif number_of_bombs == 3:
            return 'red'
        elif number_of_bombs == 4:
            return 'purple'
        else:
            return 'yellow'

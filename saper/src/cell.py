from cellbase import CellBase


class CellState:
    NOT_CLICKED = 0
    CLICKED = 1
    SURE_BOMB = 2
    MAYBE_BOMB = 3
    DEACTIVATED = 4


class Cell(CellBase):
    """
    The cell on the board. It has its state and other properties.
    """
    state = CellState.NOT_CLICKED
    value = 0
    is_bomb = False

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'    {self.value} ' \
               f': state {self.state} ' \
               f': is_bomb {"True" if self.is_bomb else "False"}    '

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_state(self, state):
        self.state = state

    """
    Right mouse click
    """

    def mark(self):
        if self.state == CellState.SURE_BOMB:
            self.state = CellState.MAYBE_BOMB
        elif self.state == CellState.MAYBE_BOMB:
            self.state = CellState.NOT_CLICKED
        else:
            self.state = CellState.SURE_BOMB

    def set_bomb(self):
        self.is_bomb = True

    def increment_value(self):
        self.value += 1

    def is_clicked(self) -> bool:
        return self.state == CellState.CLICKED

    def is_state_sure_bomb(self) -> bool:
        return self.state == CellState.SURE_BOMB

    def is_state_maybe_bomb(self) -> bool:
        return self.state == CellState.MAYBE_BOMB

    def is_deactivated(self) -> bool:
        return self.state == CellState.DEACTIVATED

    def can_be_clicked(self) -> bool:
        return not (self.is_clicked() or self.is_state_sure_bomb() or self.is_deactivated())

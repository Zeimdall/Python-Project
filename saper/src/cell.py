from cellbase import CellBase


class CellState:
    NOT_CLICKED = 0
    CLICKED = 1
    SURE_BOMB = 2
    MAYBE_BOMB = 3
    DEACTIVATED = 4


class Cell(CellBase):
    """ The cell on the board. It has its state and other properties.
     """

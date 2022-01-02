class GameState:
    MAIN_WINDOW = 0
    GAME = 1
    GAME_OVER = 2
    WIN = 3


class GameMode:
    DEFAULT = 0
    VISIBLE_BOMBS = 1


class GameManager:
    CHEAT_CODE = 'xyzzy'

    def __init__(self):
        self.n = None
        self.m = None
        self.bomb_number = None
        self.main_frame = None
        self.window_main = None
        self.board = None
        self.game_state = GameState.MAIN_WINDOW
        self.game_mode = GameMode.DEFAULT

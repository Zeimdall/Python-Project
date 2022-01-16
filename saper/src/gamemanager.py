from src.board import Board

from tkinter import *


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
        self.set_up_gui()

    def set_up_gui(self):
        """settings for application's view"""
        self.window_main = Tk(className='Saper: Game')
        self.window_main.option_add('*Font', 'Times 19')
        self.window_main.geometry("1024x760")

    def gui(self):
        """application's view"""
        def clear_frame(frame):
            """clear widgets from a tkinter frame"""
            for widgets in frame.winfo_children():
                widgets.destroy()

        def click(x, y):
            """left mouse click"""
            self.board.click_cell(x, y)

            if self.board.get_cell(x, y).is_bomb:
                self.game_state = GameState.GAME_OVER

            if self.board.is_board_win():
                self.game_state = GameState.WIN

            render_game_frame()

        def mark(x, y):
            """right mouse click"""
            self.board.mark_cell(x, y)
            self.board.update_total_set_as_bomb()

            if self.board.is_board_win():
                self.game_state = GameState.WIN

            render_game_frame()

        def play_again():
            """play again button"""
            self.board = None
            self.game_mode = GameMode.DEFAULT
            self.game_state = GameState.GAME
            render_game_frame()

        def new_game():
            """new game button"""
            self.board = None
            self.game_mode = GameMode.DEFAULT
            self.game_state = GameState.MAIN_WINDOW
            render_main_frame()

        def toggle_game_mode():
            """cheat code button"""
            if self.game_mode == GameMode.DEFAULT:
                self.game_mode = GameMode.VISIBLE_BOMBS
            else:
                self.game_mode = GameMode.DEFAULT

            render_game_frame()

        '''
        Render game frame with board and cells on it
        '''

        def render_game_frame():
            if not self.board:
                try:
                    self.board = Board(int(self.n.get()), int(self.m.get()), int(self.bomb_number.get()))
                    self.board.create_board()
                    self.board.fill_up_bombs()
                    self.game_state = GameState.GAME
                except Exception as e:
                    self.board = None
                    Label(self.main_frame, text=f"Error: {e}", fg="red").pack()

            self.board.print()
            clear_frame(self.main_frame)
            cell_buttons = []
            self.window_main.bind(GameManager.CHEAT_CODE, lambda _: toggle_game_mode())

            for x in range(self.board.n):
                cell_buttons.append([])
                for y in range(self.board.m):
                    cell_buttons[x].append(
                        Label(
                            self.main_frame,
                            text='*' if self.board.get_cell(x, y).is_bomb
                            else (
                                self.board.get_cell(x, y).value if self.board.get_cell(x, y).value > 0
                                else ''
                            ),
                            width=3,
                            height=2,
                            bg='#d3d3d3',
                            fg=Board.get_color(self.board.get_cell(x, y).value),
                            font=("Arial", 13)
                        )
                        if self.board.get_cell(x, y).is_clicked()
                           or self.board.get_cell(x, y).is_deactivated()
                           or self.game_state == GameState.WIN
                           or self.game_state == GameState.GAME_OVER
                        else
                        Button(
                            self.main_frame,
                            text=('B' if self.board.get_cell(x, y).is_state_sure_bomb()
                                  else ('?' if self.board.get_cell(x, y).is_state_maybe_bomb()
                                        else ''
                                        )
                                  ),
                            width=2,
                            height=1,
                            background='gray' if self.game_mode == GameMode.VISIBLE_BOMBS
                                                 and self.board.get_cell(x, y).is_bomb
                            else 'white'
                        )
                    )

                    if not (self.board.get_cell(x, y).is_clicked() or self.board.get_cell(x, y).is_deactivated()):
                        cell_buttons[x][y].bind("<Button-1>", lambda event, _x=x, _y=y: click(_x, _y))
                        cell_buttons[x][y].bind("<Button-2>", lambda event, _x=x, _y=y: mark(_x, _y))
                        cell_buttons[x][y].bind("<Button-3>", lambda event, _x=x, _y=y: mark(_x, _y))

                    cell_buttons[x][y].grid(row=x, column=y, sticky='nsew')

            Label(self.main_frame, text=f"Flagged: {self.board.total_set_as_bomb}") \
                .grid(row=1, column=int(self.board.m + 2), sticky='nsew')

            if self.game_state == GameState.GAME_OVER:
                Label(self.main_frame, text="Game Over :(", fg="red") \
                    .grid(row=2, column=int(self.board.m + 2), sticky='nsew')

            if self.game_state == GameState.WIN:
                Label(self.main_frame, text="You won :)", fg="green") \
                    .grid(row=2, column=int(self.board.m + 2), sticky='nsew')

            Button(
                self.main_frame,
                text="Play again",
                command=play_again,
                background='blue',
                fg='white'
            ).grid(row=0, column=int(self.board.m + 2))

            Button(
                self.main_frame,
                text="New game",
                command=new_game,
                background='green',
                fg='white'
            ).grid(row=0, column=int(self.board.m + 3))

            if self.game_state == GameState.GAME:
                Button(
                    self.main_frame,
                    text="Show bombs" if self.game_mode == GameMode.DEFAULT else "Hide bombs",
                    command=toggle_game_mode,
                    background='red',
                    fg='white'
                ).grid(row=0, column=int(self.board.m + 4))

        '''
        Render main menu frame with inputs and button to start a game
        '''

        def render_main_frame():
            self.game_state = GameState.MAIN_WINDOW

            if not self.main_frame:
                self.main_frame = Frame(self.window_main)
                self.main_frame.pack(side="top", expand=True, fill="both")

            clear_frame(self.main_frame)

            Label(self.main_frame, text="N:").pack()
            self.n = StringVar()
            Entry(self.main_frame, textvariable=self.n).pack()

            Label(self.main_frame, text="M:").pack()
            self.m = StringVar()
            Entry(self.main_frame, textvariable=self.m).pack()

            Label(self.main_frame, text="Number of bombs:").pack()
            self.bomb_number = StringVar()
            Entry(self.main_frame, textvariable=self.bomb_number).pack()

            submit = Button(
                self.main_frame,
                text="Start game",
                command=render_game_frame
            )
            submit.pack()

        render_main_frame()
        self.window_main.mainloop()

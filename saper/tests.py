import unittest
from src.gamemanager import GameManager
from src.board import Board


class tests(unittest.TestCase):

    async def _start_app(self):
        self.game_manager = GameManager()

    def setUp(self):
        self.app = GameManager()

    # Próba rozpoczęcia gry z rozmiarem planszy i liczbą min: (1 na 1; 1)
    def test_1_try_start_game_1_1_1(self):
        game_manager = GameManager()
        game_manager.board = Board(1, 1, 1)
        try:
            game_manager.board.create_board()
        except Exception:
            pass
        else:
            self.fail('ExpectedException not raised')

    # Próba rozpoczęcia gry z rozmiarem planszy i liczbą min: (5 na 1; 2)
    def test_1_try_start_game_5_1_2(self):
        game_manager = GameManager()
        game_manager.board = Board(5, 1, 2)
        try:
            game_manager.board.create_board()
        except Exception:
            pass
        else:
            self.fail('ExpectedException not raised')

    # Próba rozpoczęcia gry z rozmiarem planszy i liczbą min: (4 na 1; 2)
    def test_1_try_start_game_4_1_2(self):
        game_manager = GameManager()
        game_manager.board = Board(4, 1, 2)
        try:
            game_manager.board.create_board()
        except Exception:
            pass
        else:
            self.fail('ExpectedException not raised')

    # Próba rozpoczęcia gry z rozmiarem planszy i liczbą min: (20 na 500; 12)
    def test_1_try_start_game_20_500_12(self):
        game_manager = GameManager()
        game_manager.board = Board(20, 500, 12)
        try:
            game_manager.board.create_board()
        except Exception:
            pass
        else:
            self.fail('ExpectedException not raised')

    # Próba rozpoczęcia gry z rozmiarem planszy i liczbą min: (5 na 6; -4)
    def test_1_try_start_game_5_6_minus4(self):
        game_manager = GameManager()
        game_manager.board = Board(5, 6, -4)
        try:
            game_manager.board.create_board()
        except Exception:
            pass
        else:
            self.fail('ExpectedException not raised')

    # Próba rozpoczęcia gry z rozmiarem planszy i liczbą min: (3 na 3; 10)
    def test_1_try_start_game_3_3_10(self):
        game_manager = GameManager()
        game_manager.board = Board(3, 3, 10)
        try:
            game_manager.board.create_board()
        except Exception:
            pass
        else:
            self.fail('ExpectedException not raised')

    # Próba rozpoczęcia gry z rozmiarem planszy i liczbą min: (1 na 10; 5)
    def test_1_try_start_game_1_10_5(self):
        game_manager = GameManager()
        game_manager.board = Board(1, 10, 5)
        try:
            game_manager.board.create_board()
        except Exception:
            pass
        else:
            self.fail('ExpectedException not raised')

    # Przed kliknięciem status pola musi być równy 0
    def test_2_state_before_click(self):
        game_manager = GameManager()
        game_manager.board = Board(8, 8, 12)

        game_manager.board.create_board()
        game_manager.board.fill_up_bombs()

        self.assertEqual(game_manager.board.get_cell(1, 1).state, 0)

    # Czy działa klik - po kliknięciu status pola musi być równy 1
    def test_2_state_after_click(self):
        game_manager = GameManager()
        game_manager.board = Board(8, 8, 12)

        game_manager.board.create_board()
        game_manager.board.fill_up_bombs()

        game_manager.board.click_cell(1, 1)
        self.assertEqual(game_manager.board.get_cell(1, 1).state, 1)

    # Kliknięcie pola, wyświetla się liczba min w sąsiedztwie pola
    def test_2_after_click_show_number(self):
        game_manager = GameManager()
        game_manager.board = Board(8, 8, 12)

        game_manager.board.create_board()
        game_manager.board.fill_up_bombs()

        game_manager.board.click_cell(1, 1)
        self.assertTrue(game_manager.board.get_cell(1, 2).value >= 0)

    # Kliknięcie pola, wyświetla się mina, gra się kończy
    def test_3_check_mine_to_game_over(self):
        game_manager = GameManager()
        game_manager.board = Board(8, 8, 12)

        game_manager.board.create_board()
        game_manager.board.fill_up_bombs()

        cell = game_manager.board.get_cell(1, 1)
        cell.is_bomb = 1
        game_manager.board.click_cell(1, 1)
        self.assertTrue(game_manager.board.get_cell(1, 1).is_bomb == 1)


if __name__ == '__main__':
    unittest.main()

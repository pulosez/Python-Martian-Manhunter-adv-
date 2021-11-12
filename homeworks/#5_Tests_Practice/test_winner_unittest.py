import unittest
from game import TicTacToe


class TestGameWinner(unittest.TestCase):
    def setUp(self):
        self.game_unittest = TicTacToe()

    def test_row_unittest(self):
        print('Check row test')
        self.game_unittest.board = ['O', 'O', 'X', '0', ' ', ' ', 'X', 'X', 'X']
        self.assertTrue(self.game_unittest.winner(8, 'X'))
        self.game_unittest.print_board()

    def test_column_unittest(self):
        print('Check column test')
        self.game_unittest.board = ['X', 'O', 'X', 'X', 'O', ' ', ' ', 'O', 'X']
        self.assertTrue(self.game_unittest.winner(7, 'O'))
        self.game_unittest.print_board()

    def test_diagonal_unittest(self):
        print('Check diagonal test')
        self.game_unittest.board = ['X', 'O', 'X', '0', 'X', ' ', 'O', 'O', 'X']
        self.assertTrue(self.game_unittest.winner(8, 'X'))
        self.game_unittest.print_board()

    def test_other_condition_unittest(self):
        print('None of the above conditions are met test')
        self.game_unittest.board = ['O', 'O', 'X', '0', ' ', ' ', 'X', 'X', 'O']
        self.assertFalse(self.game_unittest.winner(2, 'O'))
        self.game_unittest.print_board()


if __name__ == '__main__':
    unittest.main()

import pytest
from game import TicTacToe


def setup_module(module):
    global game_pytest
    game_pytest = TicTacToe()


def test_row_pytest():
    print('Check row test')
    game_pytest.board = ['O', 'O', 'X', '0', ' ', ' ', 'X', 'X', 'X']
    assert game_pytest.winner(8, 'X')
    game_pytest.print_board()


def test_column_pytest():
    print('Check column test')
    game_pytest.board = ['X', 'O', 'X', 'X', 'O', ' ', ' ', 'O', 'X']
    assert game_pytest.winner(7, 'O')
    game_pytest.print_board()


def test_diagonal_pytest():
    print('Check diagonal test')
    game_pytest.board = ['X', 'O', 'X', '0', 'X', ' ', 'O', 'O', 'X']
    assert game_pytest.winner(8, 'X')
    game_pytest.print_board()


def test_other_condition_pytest():
    print('None of the above conditions are met test')
    game_pytest.board = ['O', 'O', 'X', '0', ' ', ' ', 'X', 'X', 'O']
    assert not game_pytest.winner(2, 'O')
    game_pytest.print_board()

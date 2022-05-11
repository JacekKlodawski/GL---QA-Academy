from unittest import mock
import TicTacToe.ttt.tictactoe as tc
import random


val = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


@mock.patch('builtins.input', side_effect=val)
def test_1(input):
    tc.game()

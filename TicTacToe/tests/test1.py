import unittest
from unittest import mock
import TicTacToe.ttt.tictactoe as tc
import random

#random input
val_0 = [random.choice(["1", "2", "3", "5", "4", "6", "7", "8", "9"]) for i in range(9)]
#one list for each win criteria
val_1 = ["1", "8", "2", "4", "3"]
val_2 = ["4", "2", "5", "7", "6"]
val_3 = ["7", "2", "8", "4", "9"]
val_4 = ["1", "2", "4", "9", "7"]
val_5 = ["2", "1", "5", "4", "8"]
val_6 = ["3", "2", "6", "4", "9"]
val_7 = ["1", "2", "5", "4", "9"]
val_8 = ["3", "2", "5", "4", "7"]



class Test(unittest.TestCase):
    @mock.patch('builtins.input', side_effect=val_0)
    def test_0(self, input):
        tc.game()

    @mock.patch('builtins.input', side_effect=val_1)
    def test_1(self, input):
        tc.game()

    @mock.patch('builtins.input', side_effect=val_2)
    def test_2(self, input):
        tc.game()

    @mock.patch('builtins.input', side_effect=val_3)
    def test_3(self, input):
        tc.game()

    @mock.patch('builtins.input', side_effect=val_4)
    def test_4(self, input):
        tc.game()

    @mock.patch('builtins.input', side_effect=val_5)
    def test_5(self, input):
        tc.game()

    @mock.patch('builtins.input', side_effect=val_6)
    def test_6(self, input):
        tc.game()

    @mock.patch('builtins.input', side_effect=val_7)
    def test_7(self, input):
        tc.game()

    @mock.patch('builtins.input', side_effect=val_8)
    def test_8(self, input):
        tc.game()

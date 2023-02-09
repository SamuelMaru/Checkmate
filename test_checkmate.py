import unittest

from chessthing import checkmate

"""
This is a python test suite.
You can run this to test that your checkmate function
works as expected using the command:
python test.py
Add tests as you see fit.
"""


class TestCheckmate(unittest.TestCase):
    def test_one(self):
        data = [['R', '-', 'K', '-'],
                ['R', '-', '-', '-'],
                ['-', '-', '-', '-'],
                ['-', '-', '-', '-']]
        result = checkmate(data)
        self.assertEqual(result, True)

    def test_two(self):
        data = [['-', '-', 'K', '-'],
                ['R', '-', '-', '-'],
                ['-', '-', '-', '-'],
                ['-', '-', '-', '-']]
        result = checkmate(data)
        self.assertEqual(result, False)

    def test_three(self):
        data = [['-', '-', '-', 'K'],
                ['_', '-', '-', '-'],
                ['-', '-', '-', 'R'],
                ['-', '-', 'R', '-']]
        result = checkmate(data)
        self.assertEqual(result, True)

    def test_four(self):
        data = [['-', 'R', '-', 'K'],
                ['_', '-', '-', '-'],
                ['-', '-', '-', '-'],
                ['-', '-', 'R', '-']]
        result = checkmate(data)
        self.assertEqual(result, False)

    def test_five(self):
        data = [['-', 'R', '-', 'K'],
                ['_', '-', '-', '-'],
                ['-', '-', '-', '-'],
                ['R', '-', '-', 'R']]
        result = checkmate(data)
        self.assertEqual(result, False)

    def test_no_rooks(self):
        data = [['-', '-', '-', 'K'],
                ['_', '-', '-', '-'],
                ['-', '-', '-', '-'],
                ['-', '-', '-', '-']]
        result = checkmate(data)
        self.assertEqual(result, False)

    def test_close_rooks(self):
        data = [['-', 'R', '-', 'K'],
                ['_', '-', 'R', '-'],
                ['-', '-', '-', '-'],
                ['-', '-', '-', '-']]
        result = checkmate(data)
        self.assertEqual(result, False)


unittest.main()
import unittest

from chessthing import is_checkmate

"""
This is a python test suite.
You can run this to test that your is_checkmate function
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
        result = is_checkmate(data)
        self.assertEqual(result, True)

    def test_two(self):
        data = [['-', '-', 'K', '-'],
                ['R', '-', '-', '-'],
                ['-', '-', '-', '-'],
                ['-', '-', '-', '-']]
        result = is_checkmate(data)
        self.assertEqual(result, False)

    def test_three(self):
        data = [['-', '-', '-', 'K'],
                ['-', '-', '-', '-'],
                ['-', '-', '-', 'R'],
                ['-', '-', 'R', '-']]
        result = is_checkmate(data)
        self.assertEqual(result, True)

    def test_four(self):
        data = [['-', 'R', '-', 'K'],
                ['-', '-', '-', '-'],
                ['-', '-', '-', '-'],
                ['-', '-', 'R', '-']]
        result = is_checkmate(data)
        self.assertEqual(result, False)

    def test_five(self):
        data = [['-', 'R', '-', 'K'],
                ['-', '-', '-', '-'],
                ['-', '-', '-', '-'],
                ['R', '-', '-', 'R']]
        result = is_checkmate(data)
        self.assertEqual(result, False)

    def test_no_rooks(self):
        data = [['-', '-', '-', 'K'],
                ['-', '-', '-', '-'],
                ['-', '-', '-', '-'],
                ['-', '-', '-', '-']]
        result = is_checkmate(data)
        self.assertEqual(result, False)

    def test_close_rooks(self):
        data = [['-', 'R', '-', 'K'],
                ['-', '-', 'R', '-'],
                ['-', '-', '-', '-'],
                ['-', '-', '-', '-']]
        result = is_checkmate(data)
        self.assertEqual(result, False)
    def test_bishops1(self):
        data = [['-', '-', '-', 'K'],
                ['-', '-', 'R', '-'],
                ['-', '-', '-', '-'],
                ['B', '-', '-', '-']]
        result = is_checkmate(data)
        self.assertEqual(result, False)
    def test_bishops2(self):
        data = [['-', '-', '-', 'K'],
                ['-', 'B', '-', '-'],
                ['-', 'B', 'B', '-'],
                ['-', '-', '-', '-']]
        result = is_checkmate(data)
        self.assertEqual(result, True)
    def test_bishops3(self):
        data = [['-', '-', '-', 'K'],
                ['-', 'B', '-', '-'],
                ['-', 'R', 'B', '-'],
                ['B', '-', '-', '-']]
        result = is_checkmate(data)
        self.assertEqual(result, False)


unittest.main()

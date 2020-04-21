import unittest
from matrix import Matrix


class Tests(unittest.TestCase):

    def test_add_matrix(self):
        a = Matrix([[1, 2], [3, 4]])
        b = Matrix([[5, 6], [7, 8]])
        self.assertEqual(a.add_matrix(b), [[6, 8], [10, 12]])

    def test_mult_matrix(self):
        a = Matrix([[1, 2], [3, 4]])
        b = Matrix([[5, 6], [7, 8]])
        self.assertEqual(a.mult_matrix(b), [[19, 22], [43, 50]])

    def test_mult_number(self):
        a = Matrix([[1, 2], [3, 4]])
        b = 2
        self.assertEqual(a.mult_number(b), [[2, 4], [6, 8]])

    def test_divide_number(self):
        a = Matrix([[3, 6], [9, 12]])
        b = 3
        self.assertEqual(a.divide_number(b), [[1, 2], [3, 4]])

    def test_transpose(self):
        a = Matrix([[3, 6, 9], [12, 15, 18]])
        self.assertEqual(a.transpose(), [[3, 12], [6, 15], [9, 18]])

    def test_contains_positive(self):
        a = Matrix([[3, 6, 9], [12, 15, 18]])
        self.assertTrue(a.contains(9))

    def test_contains_negative(self):
        a = Matrix([[3, 6, 9], [12, 15, 18]])
        self.assertFalse(a.contains(10))

    def test_access_by_coords(self):
        a = Matrix([[3, 6, 9], [12, 15, 18]])
        self.assertEqual(a.get_element((1, 1)), 15)



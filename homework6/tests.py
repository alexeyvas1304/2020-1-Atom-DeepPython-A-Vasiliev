import unittest
from realizations import *
from unittest.mock import patch, MagicMock
from random import randint
from time import sleep


def gen_list_slow():
    sleep(10)
    return [randint(1, 5) for _ in range(5)]


def get_list_tricky_random_list():
    lst = gen_list_slow()
    # print(lst)
    return get_new_list_tricky(lst)


class Testfunction(unittest.TestCase):
    def test_base(self):
        self.assertEqual(get_new_list_tricky([2, 3, 5, 7]), [105, 70, 42, 30])

    def test_compare(self):
        self.assertEqual(get_new_list_division([2, 3, 5, 7]), get_new_list_tricky([2, 3, 5, 7]))

    def test_type(self):
        self.assertIsInstance(get_new_list_tricky([2, 3, 5, 7]), list)

    def test_two_elements(self):
        self.assertEqual(get_new_list_tricky([2, 5]), [5, 2])

    def test_one_element(self):
        with self.assertRaises(IncorrectLengthException):
            get_new_list_tricky([2])

    def test_no_elements(self):
        with self.assertRaises(IncorrectLengthException):
            get_new_list_tricky([])

    def test_two_elements_one_zero(self):
        self.assertEqual(get_new_list_tricky([2, 0]), [0, 2])

    def test_only_zeros(self):
        self.assertEqual(get_new_list_tricky([0, 0, 0, 0]), [0, 0, 0, 0])

    def test_one_zero_element(self):
        self.assertEqual(get_new_list_tricky([1, 2, 0, 4]), [0, 0, 8, 0])

    def test_more_than_one_zero_element(self):
        self.assertEqual(get_new_list_tricky([1, 2, 0, 0]), [0, 0, 0, 0])

    def test_big_numbers(self):
        self.assertEqual(get_new_list_tricky([10 ** 25, 10 ** 35, 10 ** 100, 10 ** 20]),
                         [10 ** 155, 10 ** 145, 10 ** 80, 10 ** 160])

    def test_mock_context_manager(self):
        with patch('tests.gen_list_slow') as mocked_func:
            mocked_func.return_value = [1, 2, 3, 4, 5]
            assert get_list_tricky_random_list() == [120, 60, 40, 30, 24]

    @patch('tests.gen_list_slow', MagicMock(return_value=[1, 2, 3, 4, 5]))
    def test_mock_decorator(self):
        assert get_list_tricky_random_list() == [120, 60, 40, 30, 24]


if __name__ == '__main__':
    # print(get_list_tricky_random_list())  # медленоооо
    unittest.main()

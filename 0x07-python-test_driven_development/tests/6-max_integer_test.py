#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    

    def setUp(self):
        self.list1 = [1, 2, 3, 4]
        self.list2 = [1, 4, 2]
        self.list3 = [4, 3, 2, 1]
        self.list4 = [-1, -2, -3, -4]
        self.list5 = [-1, 2, 3, 4]
        self.list6 = []
        self.list7 = [4]


    def test_sorted_list_of_int(self):
        self.assertEqual(max_integer(self.list1), 4)


    def test_unsorted_list_of_int(self):
        self.assertEqual(max_integer(self.list2), 4)


    def test_reversed_sorted_list_of_int(self):
        self.assertEqual(max_integer(self.list3), 4)


    def test_list_of_negative_int(self):
        self.assertEqual(max_integer(self.list4), -1)


    def test_list_of_mixed_signs_of_int(self):
        self.assertEqual(max_integer(self.list5), 4)


    def test_empty_list(self):
        self.assertEqual(max_integer(self.list6), None)


    def test_list_of_one_element(self):
        self.assertEqual(max_integer(self.list7), 4)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""Unittest for Base
"""
import unittest
Base = __import__('../models/Base').Base


class TestBase(unittest.TestCase):

    def setUp(self):
        self.b1 = Base()
        self.b2 = Base(12)

    def test_id_value(self):
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)

    def test_to_json(self):
        self.assertEqual(Base.to_json_string([{'x': 0, 'y': 0}]),
                '[{"x": 0, "y": 0}]')
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string(), '[]')

if __name__ == '__main__':
    unittest.main()

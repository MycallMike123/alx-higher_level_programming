#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer"""

    def test_positive_numbers(self):
        """Test a ls with positive numbers"""

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([10, 20, 30, 40]), 40)

    def test_negative_numbers(self):
        """Test a ls with negative numbers"""

        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-11, -22, -33, -44]), -11)

    def test_mixed_numbers(self):
        """Test a ls with mixed numbers"""

        self.assertEqual(max_integer([2, -2, 3, -5]), 3)
        self.assertEqual(max_integer([-11, 24, -33, 40]), 40)

    def test_empty_list(self):
        """Test a ls with empty numbers"""

        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """Test a ls with single elements"""

        self.assertEqual(max_integer([5]), 5)

    def test_duplicate_elements(self):
        """Test a ls with dublicate elements"""

        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_float_numbers(self):
        """Test a ls with float numbers"""

        self.assertEqual(max_integer([1.3, 2.1, 3.3, 4.9]), 4.9)

    def test_string_elements(self):
        """Test a ls with strings"""

        self.assertEqual(max_integer(["apple", "banana", "orange"]), "orange")

    def test_mixed_types(self):
        """Test a ls with mixed elements"""

        with self.assertRaises(TypeError):
            max_integer([1, "two", 3, 4])

if __name__ == '__main__':
    unittest.main()

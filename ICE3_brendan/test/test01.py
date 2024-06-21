##########################################################################
# Name:         Brendan Obilo
# Reg No:       100952871
# Description:  This program is a program that will test another program that
#               accept list of integer and validate the list to be an integer
#               and then produces the minimum number as the output.
# Type of Document: In class 3
# Date:         13/06/2024
##########################################################################

# To import tha unit test library for testing
import unittest

# To import the code to test
from app.minimum import Minimum


class MinimumTest(unittest.TestCase):

    @classmethod
    def stepUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("teardownClass")

    def setUp(self):
        print("setUp")
        self.calc = Minimum()

    def tearDown(self):
        print("\ntearDown")

    # First test case that test with the size of 1, 2, or 3 elements
    def test_minimum_1(self):
        calc = Minimum()
        self.assertEqual(90, calc.minimum_number([90]))
        self.assertEqual(10, calc.minimum_number([12, 10]))
        self.assertEqual(10, calc.minimum_number([10, 12]))
        self.assertEqual(12, calc.minimum_number([12, 14, 36]))
        self.assertEqual(12, calc.minimum_number([36, 14, 12]))
        self.assertEqual(12, calc.minimum_number([14, 12, 36]))
        print("Test Case 1: A very short list (of inputs) with the size of 1, 2, or 3 elements")

    # Second test case that test with an empty list
    def test_minimum_2(self):
        calc = Minimum()
        self.assertRaises(ValueError, calc.minimum_number, ([]))
        print("Test Case 2: An empty list i.e., of size 0.")

    # Third test case that test with minimum element is the first or last element.
    def test_minimum_3(self):
        calc = Minimum()
        self.assertEqual(10, calc.minimum_number([10, 23, 34, 81, 97]))
        self.assertEqual(10, calc.minimum_number([97, 81, 34, 23, 10]))
        print("Test Case 3: A list where the minimum element is the first or last element.")

    # Fourth case where the minimum element is negative
    def test_minimum_4(self):
        calc = Minimum()
        self.assertEqual(-2, calc.minimum_number([10, -2, 5, 23]))
        self.assertEqual(-24, calc.minimum_number([10, -2, -24, 4]))
        print("Test Case 4: A list where the minimum element is negative.")

    # Fifth case where all elements are negatives
    def test_minimum_5(self):
        calc = Minimum()
        self.assertEqual(-56, calc.minimum_number([-23, -31, -45, -56]))
        self.assertEqual(-203, calc.minimum_number([-6, -203, -2, -78]))
        print("Test Case 5: A list where all elements are negative.")

    # The Sixth Case where some elements are real numbers
    def test_minimum_6(self):
        calc = Minimum()
        self.assertRaises(TypeError, calc.minimum_number, ([23, 34.56, 67, 33]))
        print("Test Case 6: A list where some elements are real numbers.")

    # The seventh Test Case where the element is alphabet or special character
    def test_minimum_7(self):
        calc = Minimum()
        self.assertRaises(TypeError, calc.minimum_number, ([23, "hi", 32, 1]))
        self.assertRaises(TypeError, calc.minimum_number, ([12, "&", "*", "34m", "!"]))
        print("Test Case 7: A list where some elements are alphabetic characters and special characters.")

    # The eight case where the element has a duplicate number
    def test_minimum_8(self):
        calc = Minimum()
        self.assertEqual(3, calc.minimum_number([3, 4, 6, 9, 6]))
        self.assertEqual(6, calc.minimum_number([13, 6, 6, 9, 15]))
        print("Test Case 8: A list with duplicate elements")

    # The Ninth test case where the one number is greater than the expected maximum
    def test_minimum_9(self):
        calc = Minimum()
        self.assertEqual(23, calc.minimum_number([530, 429449672, 97, 23, 46, 59]))
        print("Test Case 9: A list where one element has a value greater than the maximum permissible ")


if __name__ == '__main__':
    unittest.main()

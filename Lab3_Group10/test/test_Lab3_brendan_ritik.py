##########################################################################
# Name:         Brendan Obilo
#               Ritik Sharma
# Reg No:       100952871
#               100952840
# Description:  This program is a project that finds the areas of different shapes
#               along with its test cases file along with fixtures which calculates
#               the areas of four shapes: Circle, Trapezium, Ellipse, and Rhombus.
# Type of Document: Lab 3 Group 10
# Date:         21/06/2024
##########################################################################


# To import tha unit test library for testing
import unittest

# To import the code to test
from app.Lab3_brendan_ritik import AREA


class AreaTest(unittest.TestCase):

    @classmethod
    def stepUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("teardownClass")

    def setUp(self):
        print("setUp")
        self.calc = AREA()

    def tearDown(self):
        print("\ntearDown")

    # Circle First test case that test when radius is greater than 0
    def test_circle_1(self):
        self.assertEqual(3.14, self.calc.area_of_circle([1]))
        self.assertEqual(12.57, self.calc.area_of_circle([2]))
        self.assertEqual(153.94, self.calc.area_of_circle([7]))
        self.assertEqual(226.98, self.calc.area_of_circle([8.5]))
        self.assertEqual(38.48, self.calc.area_of_circle([3.5]))
        print("End of test: Test areas when radius is greater than 0")

    # Circle Second test case that test with radius less than or equal to 0
    def test_circle_2(self):
        self.assertRaises(ValueError, self.calc.area_of_circle, ([-3]))
        self.assertRaises(ValueError, self.calc.area_of_circle, ([-4]))
        self.assertRaises(ValueError, self.calc.area_of_circle, ([0]))
        self.assertRaises(ValueError, self.calc.area_of_circle, ([-2.5]))
        print("End of test: Test areas when radius is less than or equal to 0")

    # Circle Third test case that test with radius boolean value or complex/imaginary value or text
    def test_circle_3(self):
        self.assertRaises(TypeError, self.calc.area_of_circle, ([2+5j]))
        self.assertRaises(TypeError, self.calc.area_of_circle, (["$"]))
        self.assertRaises(TypeError, self.calc.area_of_circle, ([True]))
        self.assertRaises(TypeError, self.calc.area_of_circle, ([False]))
        self.assertRaises(TypeError, self.calc.area_of_circle, (["brendanritik"]))
        print("End of test: Test areas when radius is boolean value or complex/imaginary value or text")

    # Circle Fourth test case that test with no radius input or more than one parameter
    def test_circle_4(self):
        self.assertRaises(ValueError, self.calc.area_of_circle, ([]))
        self.assertRaises(ValueError, self.calc.area_of_circle, ([3, 4]))
        print("End of test: Test areas when no input for radius or more than one parameter")

    # Trapezium First test case that test when parameters is greater than 0
    def test_trapezium_1(self):
        self.assertEqual(4.5, self.calc.area_of_trapezium([1, 2, 3]))
        self.assertEqual(112.5, self.calc.area_of_trapezium([5, 10, 15]))
        self.assertEqual(43.75, self.calc.area_of_trapezium([5.3, 12.2, 5]))
        print("End of test: Test areas when parameters is greater than 0")

    # Trapezium Second test case that test with any parameter less than or equal to 0
    def test_trapezium_2(self):
        self.assertRaises(ValueError, self.calc.area_of_trapezium, ([-3, 5, 0]))
        self.assertRaises(ValueError, self.calc.area_of_trapezium, ([-4, 4.2, -19]))
        self.assertRaises(ValueError, self.calc.area_of_trapezium, ([-5, -4, -3.5]))
        print("End of test: Test areas when any parameter is less than or equal to 0")

    # Trapezium Third test case that test with any parameter boolean value or complex/imaginary value or text
    def test_trapezium_3(self):
        self.assertRaises(TypeError, self.calc.area_of_trapezium, ([5, True, 2]))
        self.assertRaises(TypeError, self.calc.area_of_trapezium, ([2+5j, 4.2, 2]))
        self.assertRaises(TypeError, self.calc.area_of_trapezium, (["ritikbrendan", -5, "!"]))
        self.assertRaises(TypeError, self.calc.area_of_trapezium, ([3+7j, False, "ritikbrendan"]))
        print("End of test: Test areas when any parameter is boolean or complex/imaginary value or text")

    # Trapezium Fourth test case that test with any parameter is nothing, more or less than expected
    def test_trapezium_4(self):
        self.assertRaises(ValueError, self.calc.area_of_trapezium, ([]))
        self.assertRaises(ValueError, self.calc.area_of_trapezium, ([1]))
        self.assertRaises(ValueError, self.calc.area_of_trapezium, ([2, 3]))
        self.assertRaises(ValueError, self.calc.area_of_trapezium, ([2, 3, 4, 5]))
        print("End of test: Test areas when any parameter is nothing, more or less than expected")

    # Ellipse First test case that test when parameters is greater than 0
    def test_ellipse_1(self):
        self.assertEqual(3.14, self.calc.area_of_ellipse([1, 1]))
        self.assertEqual(49.95, self.calc.area_of_ellipse([5.3, 3]))
        self.assertEqual(37.70, self.calc.area_of_ellipse([3, 4]))
        self.assertEqual(7.85, self.calc.area_of_ellipse([0.5, 5]))
        print("End of test: Test areas when parameters is greater than 0")

    # Ellipse Second test case that test with any parameter less than or equal to 0
    def test_ellipse_2(self):
        self.assertRaises(ValueError, self.calc.area_of_ellipse, ([-1, 0]))
        self.assertRaises(ValueError, self.calc.area_of_ellipse, ([-5, -3]))
        self.assertRaises(ValueError, self.calc.area_of_ellipse, ([3, -4.2]))
        self.assertRaises(ValueError, self.calc.area_of_ellipse, ([0, 5.1]))
        print("End of test: Test areas when any parameter is less than or equal to 0")

    # Ellipse Third test case that test with any parameter boolean value or complex/imaginary value or text
    def test_ellipse_3(self):
        self.assertRaises(TypeError, self.calc.area_of_ellipse, ([5, True]))
        self.assertRaises(TypeError, self.calc.area_of_ellipse, ([2+5j, False]))
        self.assertRaises(TypeError, self.calc.area_of_ellipse, (["ritikbrendan", -5]))
        self.assertRaises(TypeError, self.calc.area_of_ellipse, (["*", "ritikbrendan"]))
        print("End of test: Test areas when any parameter is boolean or complex/imaginary value or text")

    # Ellipse Fourth test case that test with any parameter is nothing, more or less than expected
    def test_ellipse_4(self):
        self.assertRaises(ValueError, self.calc.area_of_ellipse, ([]))
        self.assertRaises(ValueError, self.calc.area_of_ellipse, ([5]))
        self.assertRaises(ValueError, self.calc.area_of_ellipse, ([3, 4, 5.3]))
        print("End of test: Test areas when any parameter is nothing, more or less than expected")

    # Rhombus First test case that test when parameters is greater than 0
    def test_rhombus_1(self):
        self.assertEqual(1, self.calc.area_of_rhombus([1, 1]))
        self.assertEqual(16.2, self.calc.area_of_rhombus([3, 5.4]))
        self.assertEqual(12, self.calc.area_of_rhombus([3, 4]))
        self.assertEqual(2.5, self.calc.area_of_rhombus([0.5, 5]))
        print("Test Case 1: First test case that test when parameters is greater than 0")

    # Ellipse Second test case that test with any parameter less than or equal to 0
    def test_rhombus_2(self):
        self.assertRaises(ValueError, self.calc.area_of_rhombus, ([-1, 0]))
        self.assertRaises(ValueError, self.calc.area_of_rhombus, ([-5, -3]))
        self.assertRaises(ValueError, self.calc.area_of_rhombus, ([3, -4.2]))
        self.assertRaises(ValueError, self.calc.area_of_rhombus, ([0, 5.1]))
        print("End of test: Test areas when any parameter is less than or equal to 0")

    # Ellipse Third test case that test with any parameter boolean value or complex/imaginary value or text
    def test_rhombus_3(self):
        self.assertRaises(TypeError, self.calc.area_of_rhombus, ([5, True]))
        self.assertRaises(TypeError, self.calc.area_of_rhombus, ([2+5j, False]))
        self.assertRaises(TypeError, self.calc.area_of_rhombus, (["ritikbrendan", "@"]))
        self.assertRaises(TypeError, self.calc.area_of_rhombus, ([3+7j, "ritikbrendan"]))
        print("End of test: Test areas when any parameter is boolean or complex/imaginary value or text")

    # Ellipse Fourth test case that test with any parameter is nothing, more or less than expected
    def test_rhombus_4(self):
        self.assertRaises(ValueError, self.calc.area_of_rhombus, ([]))
        self.assertRaises(ValueError, self.calc.area_of_rhombus, ([5]))
        self.assertRaises(ValueError, self.calc.area_of_rhombus, ([3, 4, 5.3]))
        print("End of test: Test areas when any parameter is nothing, more or less than expected")


if __name__ == '__main__':
    unittest.main()

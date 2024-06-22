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

import unittest


from test_Lab3_brendan_ritik import AreaTest

# Declare and initialize constants to hold the value of menu option
# To establish a constant to hold the value of the quit option
QUIT = 'q'
# To establish a constant to hold the value of the area of the circle test option
CIRCLE = 'c'
# To establish a constant to hold the value of the area of the trapezium test option
TRAPEZIUM = 't'
# To establish a constant to hold the value of the area of the ellipse test option
ELLIPSE = 'e'
# To establish a constant to hold the value of the area of the rhombus test option
RHOMBUS = 'r'

while True:
    # To ask user to select option from the menu
    choice = input("""\nPlease enter one of the following options:
    - 'c' for testing area of circle
    - 't' for testing area of trapezium
    - 'e' for testing area of ellipse
    - 'r' for testing area of rhombus
    - 'q' to quit
    What would you like to do? """)

    # To ensure the user entered the quit option then end the program
    if choice.strip().lower() == QUIT:
        break
    # To check if the user entered a valid option
    elif choice.strip().lower() in {CIRCLE, TRAPEZIUM, ELLIPSE, RHOMBUS}:
        suite = unittest.TestSuite()
        # To ensure the user entered the circle test case option
        if choice.strip().lower() == CIRCLE:
            suite.addTest(AreaTest('test_circle_1'))
            suite.addTest(AreaTest('test_circle_2'))
            suite.addTest(AreaTest('test_circle_3'))
            suite.addTest(AreaTest('test_circle_4'))
        # To ensure the user entered the Trapezium test case option
        elif choice.strip().lower() == TRAPEZIUM:
            suite.addTest(AreaTest('test_trapezium_1'))
            suite.addTest(AreaTest('test_trapezium_2'))
            suite.addTest(AreaTest('test_trapezium_3'))
            suite.addTest(AreaTest('test_trapezium_4'))
        # To ensure the user entered the ellipse test case option
        elif choice.strip().lower() == ELLIPSE:
            suite.addTest(AreaTest('test_ellipse_1'))
            suite.addTest(AreaTest('test_ellipse_2'))
            suite.addTest(AreaTest('test_ellipse_3'))
            suite.addTest(AreaTest('test_ellipse_4'))
        # To ensure the user entered the rhombus test case option
        elif choice.strip().lower() == RHOMBUS:
            suite.addTest(AreaTest('test_rhombus_1'))
            suite.addTest(AreaTest('test_rhombus_2'))
            suite.addTest(AreaTest('test_rhombus_3'))
            suite.addTest(AreaTest('test_rhombus_4'))
        # execute the test
        unittest.TextTestRunner().run(suite)
    # The user did not select a valid option
    else:
        print("Please enter the correct option")

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
import math

# A constant that is used to calculate the area of a trapezium
TRAPEZIUM_CONSTANT = 0.5

# A constant to hold value of the lower boundary of range that any parameter should not reach
MINIMUM_PARAMETER = 0


class AREA(object):
    # A function that runs the entire program
    @staticmethod
    def area_of_circle(radius):
        # To ensure the user input is not empty or not more than required
        if len(radius) != 1:
            # Display to the user that input must be one radius
            raise ValueError("Input one radius value")
        else:
            # check the input in the list and validate the data type
            for element in radius:
                # check the value to ensure the required data type entered
                if type(element) is not int and type(element) is not float:
                    # throw an error to invalid for format
                    raise TypeError("The element is an invalid format")
                # check the value of the radius to be greater than 0
                elif element <= MINIMUM_PARAMETER:
                    raise ValueError("Radius must be greater than 0")
            # calculate the area of a circle
            result = round(math.pi * pow(radius[0], 2), 2)
            # display the result of the area of the circle
            return result

    @staticmethod
    def area_of_trapezium(parameters):
        # a variable to hold the expected number of parameters
        expected_parameters = 3
        # To ensure the user input has expected number of parameter
        if len(parameters) != expected_parameters:
            # Display to the user that input is expected to be three parameters
            raise ValueError("Input expect three inputs for two sides and height")
        else:
            # check all the input in the list and validate the data type
            for element in parameters:
                # check the value to be sure it is the required data type entered
                if type(element) is not int and type(element) is not float:
                    # throw an error to invalid for format
                    raise TypeError("The parameter is an invalid data type")
                # check the value of the parameter to be greater than 0
                elif element <= MINIMUM_PARAMETER:
                    # throw an error to invalid range of input
                    raise ValueError("The parameter must be greater than 0")
            # calculate the area of a trapezium
            result = round(TRAPEZIUM_CONSTANT * (parameters[0] + parameters[1]) * parameters[2], 2)
            # return the result of the area of the trapezium
            return result

    @staticmethod
    def area_of_ellipse(parameters):
        # expected number of parameters
        expected_parameters = 2
        # To ensure the user input has expected number of parameter
        if len(parameters) != expected_parameters:
            # Display to the user that input is expected to be two
            raise ValueError("Input is expected to be two parameters")
        else:
            # check all the input in the list and validate the data type
            for element in parameters:
                # check the value to be sure it is the required data type entered
                if type(element) is not int and type(element) is not float:
                    # throw an error to invalid for format
                    raise TypeError("The element is an invalid format")
                # check the value of the parameter to be greater than 0
                elif element <= MINIMUM_PARAMETER:
                    # throw an error to invalid range of input
                    raise ValueError("The parameter must be greater than 0")
            # calculate the area of an ellipse
            result = round(math.pi * parameters[0] * parameters[1], 2)
            # return the result of the area of the ellipse
            return result

    @staticmethod
    def area_of_rhombus(parameters):
        # expected number of parameters
        expected_parameters = 2
        # To ensure the user input has expected number of parameter
        if len(parameters) != expected_parameters:
            # Display to the user that input is expected to be two
            raise ValueError("Input is expected to be two parameters")
        else:
            # check all the input in the list and validate the data type
            for element in parameters:
                # check the value to be sure it is required data type entered
                if type(element) is not int and type(element) is not float:
                    # throw an error to invalid for format
                    raise TypeError("The element is an invalid format")
                # check the value of the parameter to be greater than 0
                elif element <= MINIMUM_PARAMETER:
                    # throw an error to invalid range of input
                    raise ValueError("The parameter must be greater than 0")
            # calculate the area of a rhombus
            result = round(parameters[0] * parameters[1], 2)
            # return the result of the area of the rhombus
            return result

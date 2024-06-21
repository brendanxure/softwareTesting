##########################################################################
# Name:         Brendan Obilo
# Reg No:       100952871
# Description:  This program is a program that will accept list of integer
#               and validate the list to be an integer and
#               then produces the minimum number as the output.
# Type of Document: In class 3
# Date:         13/06/2024
##########################################################################


class Minimum(object):

    # A function that runs the entire program
    @staticmethod
    def minimum_number(numbers):
        try:
            # To ensure the user input is not empty
            if len(numbers) == 0:
                # Display to the user that input is empty
                raise ValueError("Input can not be empty")
            else:
                # check all the input in the list of strings and validate the data type
                for elements in numbers:
                    # ensure it is not a type of string or float
                    if type(elements) is float or type(elements) is str:
                        # throw an error to invalid for format
                        raise TypeError("The element is an invalid format")
                # sort the new list of numbers in ascending order
                numbers.sort()
                # display the lowest number which is the first in the list
                return numbers[0]
        except ValueError:
            # To catch error for data type and display to the user
            raise ValueError("Please enter a valid integer")

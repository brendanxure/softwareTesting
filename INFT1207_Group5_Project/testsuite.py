# Name:         Brendan Obilo
#               Ritik Sharma
#               Amisha Gharti Magar
#               Surakshya Pokharel
# Reg No:       100952871
#               100952840
#               100944725
#               100951538
# Description:  A program that automatically open Chrome browser, navigates
#               to a demo Banking Site and test all required fields to confirm required result
#               with actual result
# Type of Document: Group 5 Project
# Date:         15/08/2024
##########################################################################

import unittest


from test_group5_project import TestGroup5

# Start an infinite loop to keep the program running until the user decides to quit
while True:
    # Display a menu of test case options for the user
    print("\nSelect a test case to run:")
    print("1. Test Case New Customer")
    print("2. Test Case Edit Customer")
    print("3. Test Case Delete Customer")
    print("4. Test Case New Account")
    print("5. Test Case Edit Account")
    print("6. Test Case Delete Account")
    print("7. Test Case Balance Enquiry")
    print("8. Test Case Mini Statement")
    print("9. Test Case Customized Statement")
    print("0. Quit")

    # Prompt the user to select a test case or quit the program
    choice = input("Enter the number of the test case (or 0 to quit): ")
    # Exit the loop if the user chooses to quit
    if choice == "0":
        break
    # If the user's choice is valid (between 1 and 9), run the test cases for the option selected
    elif choice in {'1', '2', '3', '4', '5', '6', '7', '8', '9'}:
        suite = unittest.TestSuite()
        # New Customer test cases
        if choice == '1':
            suite.addTest(TestGroup5('test_NC1'))
            suite.addTest(TestGroup5('test_NC2'))
            suite.addTest(TestGroup5('test_NC3'))
            suite.addTest(TestGroup5('test_NC4'))
            suite.addTest(TestGroup5('test_NC5'))
            suite.addTest(TestGroup5('test_NC6'))
            suite.addTest(TestGroup5('test_NC7'))
            suite.addTest(TestGroup5('test_NC8'))
            suite.addTest(TestGroup5('test_NC9'))
            suite.addTest(TestGroup5('test_NC_10'))
            suite.addTest(TestGroup5('test_NC_11'))
            suite.addTest(TestGroup5('test_NC_12'))
            suite.addTest(TestGroup5('test_NC_13'))
            suite.addTest(TestGroup5('test_NC_14'))
            suite.addTest(TestGroup5('test_NC_15'))
            suite.addTest(TestGroup5('test_NC_16'))
            suite.addTest(TestGroup5('test_NC_17'))
            suite.addTest(TestGroup5('test_NC_18'))
            suite.addTest(TestGroup5('test_NC_19'))
            suite.addTest(TestGroup5('test_NC_20'))
            suite.addTest(TestGroup5('test_NC_21'))
            suite.addTest(TestGroup5('test_NC_22'))
            suite.addTest(TestGroup5('test_NC_23'))
            suite.addTest(TestGroup5('test_NC_24'))
            suite.addTest(TestGroup5('test_NC_25'))
            suite.addTest(TestGroup5('test_NC_26'))
            suite.addTest(TestGroup5('test_NC_27'))
            suite.addTest(TestGroup5('test_NC_28'))

        # Edit Customer test cases
        elif choice == '2':
            suite.addTest(TestGroup5('test_EC1'))
            suite.addTest(TestGroup5('test_EC2'))
            suite.addTest(TestGroup5('test_EC3'))
            suite.addTest(TestGroup5('test_EC4'))
            suite.addTest(TestGroup5('test_EC5'))
            suite.addTest(TestGroup5('test_EC6'))
            suite.addTest(TestGroup5('test_EC7'))
            suite.addTest(TestGroup5('test_EC8'))
            suite.addTest(TestGroup5('test_EC9'))
            suite.addTest(TestGroup5('test_EC_10'))
            suite.addTest(TestGroup5('test_EC_11'))
            suite.addTest(TestGroup5('test_EC_12'))
            suite.addTest(TestGroup5('test_EC_13'))
            suite.addTest(TestGroup5('test_EC_14'))
            suite.addTest(TestGroup5('test_EC_15'))
            suite.addTest(TestGroup5('test_EC_16'))
            suite.addTest(TestGroup5('test_EC_17'))
            suite.addTest(TestGroup5('test_EC_18'))
            suite.addTest(TestGroup5('test_EC_19'))
            suite.addTest(TestGroup5('test_EC_20'))

        # Delete Customer test cases
        elif choice == '3':
            suite.addTest(TestGroup5('test_DC1'))
            suite.addTest(TestGroup5('test_DC2'))
            suite.addTest(TestGroup5('test_DC3'))
            suite.addTest(TestGroup5('test_DC4'))
            suite.addTest(TestGroup5('test_DC5'))
            suite.addTest(TestGroup5('test_DC6'))
            suite.addTest(TestGroup5('test_DC7'))
            suite.addTest(TestGroup5('test_DC8'))

        # New Account test cases
        elif choice == '4':
            suite.addTest(TestGroup5('test_NA1'))
            suite.addTest(TestGroup5('test_NA2'))
            suite.addTest(TestGroup5('test_NA3'))
            suite.addTest(TestGroup5('test_NA4'))
            suite.addTest(TestGroup5('test_NA5'))
            suite.addTest(TestGroup5('test_NA6'))
            suite.addTest(TestGroup5('test_NA7'))
            suite.addTest(TestGroup5('test_NA8'))
            suite.addTest(TestGroup5('test_NA9'))
            suite.addTest(TestGroup5('test_NA_10'))
            suite.addTest(TestGroup5('test_NA_11'))
            suite.addTest(TestGroup5('test_NA_12'))
            suite.addTest(TestGroup5('test_NA_13'))
            suite.addTest(TestGroup5('test_NA_14'))
            suite.addTest(TestGroup5('test_NA_15'))
            suite.addTest(TestGroup5('test_NA_16'))

        # Edit Account test cases
        elif choice == '5':
            suite.addTest(TestGroup5('test_EA1'))
            suite.addTest(TestGroup5('test_EA2'))
            suite.addTest(TestGroup5('test_EA3'))
            suite.addTest(TestGroup5('test_EA4'))
            suite.addTest(TestGroup5('test_EA5'))
            suite.addTest(TestGroup5('test_EA6'))
            suite.addTest(TestGroup5('test_EA7'))
            suite.addTest(TestGroup5('test_EA8'))

        # Delete Account test cases
        elif choice == '6':
            suite.addTest(TestGroup5('test_DA1'))
            suite.addTest(TestGroup5('test_DA2'))
            suite.addTest(TestGroup5('test_DA3'))
            suite.addTest(TestGroup5('test_DA4'))
            suite.addTest(TestGroup5('test_DA5'))
            suite.addTest(TestGroup5('test_DA6'))
            suite.addTest(TestGroup5('test_DA7'))
            suite.addTest(TestGroup5('test_DA8'))

        # Balance Enquiry test cases
        elif choice == '7':
            suite.addTest(TestGroup5('test_BE1'))
            suite.addTest(TestGroup5('test_BE2'))
            suite.addTest(TestGroup5('test_BE3'))
            suite.addTest(TestGroup5('test_BE4'))
            suite.addTest(TestGroup5('test_BE5'))
            suite.addTest(TestGroup5('test_BE6'))
            suite.addTest(TestGroup5('test_BE7'))

        # Mini Statement test cases
        elif choice == '8':
            suite.addTest(TestGroup5('test_MS1'))
            suite.addTest(TestGroup5('test_MS2'))
            suite.addTest(TestGroup5('test_MS3'))
            suite.addTest(TestGroup5('test_MS4'))
            suite.addTest(TestGroup5('test_MS5'))
            suite.addTest(TestGroup5('test_MS6'))
            suite.addTest(TestGroup5('test_MS7'))
            suite.addTest(TestGroup5('test_MS8'))

        # Customized Statement test cases
        elif choice == '9':
            suite.addTest(TestGroup5('test_CS1'))
            suite.addTest(TestGroup5('test_CS2'))
            suite.addTest(TestGroup5('test_CS3'))
            suite.addTest(TestGroup5('test_CS4'))
            suite.addTest(TestGroup5('test_CS5'))
            suite.addTest(TestGroup5('test_CS6'))
            suite.addTest(TestGroup5('test_CS7'))
            suite.addTest(TestGroup5('test_CS8'))
            suite.addTest(TestGroup5('test_CS9'))
            suite.addTest(TestGroup5('test_CS_10'))
            suite.addTest(TestGroup5('test_CS_11'))
            suite.addTest(TestGroup5('test_CS_12'))
            suite.addTest(TestGroup5('test_CS_13'))
            suite.addTest(TestGroup5('test_CS_14'))
            suite.addTest(TestGroup5('test_CS_15'))
            suite.addTest(TestGroup5('test_CS_16'))
            suite.addTest(TestGroup5('test_CS_17'))

        # Execute the test suite using a text-based test runner
        unittest.TextTestRunner().run(suite)
    # If the user enters an invalid choice, prompt them to enter a correct option
    else:
        print("Please enter the correct option")

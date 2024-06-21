import unittest


from test01 import MinimumTest


while True:
    print("\nSelect a test case to run:")
    print("1. Test Case 01")
    print("2. Test Case 02")
    print("3. Test Case 03")
    print("4. Test Case 04")
    print("5. Test Case 05")
    print("6. Test Case 06")
    print("7. Test Case 07")
    print("8. Test Case 08")
    print("9. Test Case 09")
    print("0. Quit")

    choice = input("Enter the number of the test case (or 0 to quit):")
    if choice == "0":
        break
    elif choice in {'1', '2', '3', '4', '5', '6', '7', '8', '9'}:
        suite = unittest.TestSuite()
        if choice == '1':
            suite.addTest(MinimumTest('test_minimum_1'))
        elif choice == '2':
            suite.addTest(MinimumTest('test_minimum_2'))
        elif choice == '3':
            suite.addTest(MinimumTest('test_minimum_3'))
        elif choice == '4':
            suite.addTest(MinimumTest('test_minimum_4'))
        elif choice == '5':
            suite.addTest(MinimumTest('test_minimum_5'))
        elif choice == '6':
            suite.addTest(MinimumTest('test_minimum_7'))
        elif choice == '7':
            suite.addTest(MinimumTest('test_minimum_8'))
        elif choice == '9':
            (suite.addTest(MinimumTest('test_minimum_9')))

        # execute the test
        unittest.TextTestRunner().run(suite)
    else:
        print("Please enter the correct option")

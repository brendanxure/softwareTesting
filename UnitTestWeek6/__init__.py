__author__ = 'Dr.Sukhwant Sagar'

# Steps
# 1. You have understood the concept of unit testing in Week 5 and created few basic tests too.
# 2. Learn few concepts of Assertions in test cases - test_assertion1.py to test_assertion2.py
# 3. Now try out all functions of calculator and set up its test cases. The application file name is
# calculatorfunctions.py and test file name is test_calculatorfunctions.py. Exceptions can be thrown in
# two ways - one normally and other with context manager
# 4.Create a test file with methods of Test Case Class - setup() and teardown(), we are going to give the
# name of the file as test_calculatorfunctions_fixtures.py
# 5. Create a test file with testsuite() method of the Test Case class.
    # Steps of creating test suite
    # Step 1 − Create an instance of TestSuite class.
    #        suite = unittest.TestSuite()
    #   Step 2 − Add tests inside a TestCase class in the suite.
    #        suite.addTest(testcase class)
    #    Step 3 − You can also use makeSuite() method to add tests from a class
    #        suite = unittest.makeSuite(test case class)
    #   Step 4 − Individual tests can also be added in the suite.
    #       suite.addTest(testcaseclass("testmethod")
    #   Step 5 − Create an object of the TestTestRunner class.
    #       runner = unittest.TextTestRunner()
    #   Step 6 − Call the run() method to run all the tests in the suite
    #       runner.run (suite)
# 6. Lets write one more problem: Create basic test on employee class Employee class has three parameters
# firstname, last name and pay.
# 7. Improve the test file for employee with fixtures.

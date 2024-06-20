import unittest


class TestClass01(unittest.TestCase):
    # If you don't name these test cases with test prefix, the modules won't be tested for conditions
    def test_case01(self):
        self.assertTrue("PYTHON".isupper())
        print("\nIn test_case1()")

    def test_case02(self):
        self.assertTrue("Python".isupper())  # change to islower(), then change python in lower case-
        # then all test cases are successful
        print("\nIn test_case2()")

    def test_split(self):
        # s = '23'     # AssertionError: Lists differ: ['23'] != ['hello', 'world']

        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])


if __name__ == '__main__':
    unittest.main()

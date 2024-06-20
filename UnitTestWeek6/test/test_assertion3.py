import unittest

import math


class SimpleTest(unittest.TestCase):

    def test1(self):
        self.assertAlmostEqual(22.0/7, 3.14)

    def test2(self):
        self.assertNotAlmostEqual(10.0/3, 3)

    def test3(self):
        self.assertGreater(math.pi, 3)

    def test4(self):
        self.assertNotRegexpMatches("The sales are up by 10 Point", "Point")  # Test Failure
        # self.assertNotRegexpMatches("The sales are up by 10 Point", "percent")  # Test Passed

if __name__ == '__main__':
    unittest.main()

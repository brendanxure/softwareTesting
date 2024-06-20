import unittest


class SuiteTest(unittest.TestCase):
    a = 50
    b = 40

    def test_add(self):
        """Add"""
        result = self.a + self.b
        self.assertEqual(result, 100)

    @unittest.skipIf(a < b, "Skip over this routine")  # change it to a>b, this test will be skipped
    def test_sub(self):
        """sub"""
        result = self.a - self.b
        self.assertTrue(result == 10)
        print("Subtraction successful")

    @unittest.skipUnless(b == 0, "Skip over this routine")  # change value above of b to 0 and you will get
    # an error message because this test case will be run.
    def test_div(self):
        """div"""
        result = self.a / self.b
        self.assertTrue(result == 1)


if __name__ == '__main__':
    unittest.main()

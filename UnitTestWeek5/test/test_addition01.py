import unittest

from app.addition01 import Addition01


class TestAddition01(unittest.TestCase):
    def test_add_method_returns_correct_result(self):
        calc = Addition01()
        self.assertEqual(4, calc.add(2, 2))

    def test_add_method_raises_typeerror_if_not_ints(self):
        calc = Addition01()
        self.assertRaises(TypeError, calc.add, "Hello", "World")


if __name__ == '__main__':
    unittest.main()

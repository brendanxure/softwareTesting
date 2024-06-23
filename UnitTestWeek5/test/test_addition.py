import unittest

from app.addition import Addition


class TestAddition(unittest.TestCase):
    def test_add_method_returns_correct_result(self):
        calc = Addition()
        self.assertEqual(4, calc.add(2, 2))

    def test_add_method_raises_typeerror_if_not_ints(self):
        calc = Addition()
        self.assertRaises(TypeError, calc.add, "Hello", "World")


if __name__ == '__main__':
    unittest.main()

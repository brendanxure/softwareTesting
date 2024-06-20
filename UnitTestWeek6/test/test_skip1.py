import unittest


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


class SimpleTest(unittest.TestCase):
    @unittest.skip("Demonstrating skipping")
    def test_add(self):
        self.assertEquals(add(4, 5), 9)

    def test_sub(self):
        self.assertEquals(sub(4, 5), -1)


if __name__ == '__main__':
    unittest.main()

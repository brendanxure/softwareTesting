
class Addition(object):

    @staticmethod
    def add(x, y):

        return x + y


if __name__ == '__main__':
    calc = Addition()
    result = calc.add(2, 2)

    print(result)

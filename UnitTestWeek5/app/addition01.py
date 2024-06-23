class Addition01(object):

    @staticmethod
    def add(x, y):
        if type(x) is int and type(y) is int:
            return x + y
        else:
            raise TypeError("Invalid type: {} and {}".format(type(x), type(y)))


if __name__ == '__main__':
    calc = Addition01()
    result = calc.add(2, 2)

    print(result)

#!python3


def basicCalculate(first, second):
    print("x = {}, y = {}".format(first, second))
    print("Addition      : x + y = {}".format(first + second))
    print("Subtraction   : x - y = {}".format(first - second))
    print("Multiplication: x * y = {}".format(first * second))
    if second != 0:
        result = float(first) / second
        print("Division      : x / y = {:0.2f}".format(result))
    else:
        print("Can not divided to zero!")


basicCalculate(10, 3)

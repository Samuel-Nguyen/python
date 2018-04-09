#!python3


def calculatedMoney(first, second):
    print("Amount  = {} * {} = {}".format(first, second, first * second))


if __name__ == '__main__':
    first = int(input("Quantity: "))
    second = int(input("Prices  : "))
    calculatedMoney(first, second)

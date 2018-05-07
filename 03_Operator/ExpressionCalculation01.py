#!python3
import imp
Utils = imp.load_source("Utils", "./Utility/Utils.py")


def expressionCalculation(number):
    result = 1 + number + float(pow(number, 3)) / 3 + float(pow(number, 5)) / 5
    return result


if __name__ == '__main__':
    number = 0
    number = Utils.validateIntInput("Please input number: ", number)
    number = expressionCalculation(number)
    notification = "S = 1 + x + x^3 / 3 + x^5 / 5 = {:0.2f}".format(number)
    print(notification)

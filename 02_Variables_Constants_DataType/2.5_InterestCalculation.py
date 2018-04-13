#!python3
import sys

sys.path.append("D:\\Samuel\\Example\\PyTon\\Utils")
import Utils    # noqa


def InterestCalculation(rate, base, month):
    """
    Calculation interest base on base money, rate and month
    """
    interest = float(base * month * rate / 12 / 100)
    print("Interest = {:0.2f}".format(interest))
    print("Base money + interest = {} + {:0.2f} = {:0.2f}".format(
        base, interest, base + interest))


if __name__ == "__main__":
    rate = base = month = 0
    rate = Utils.validatePositiveFloatInput("Input rate per year (%): ", rate)
    base = Utils.validatePositiveIntInput("Input base money: ", base)
    month = Utils.validatePositiveIntInput("Input month: ", month)

    InterestCalculation(rate, base, month)

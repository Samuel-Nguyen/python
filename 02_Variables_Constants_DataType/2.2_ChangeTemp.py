#!python3
import sys

sys.path.append("D:\\Samuel\\Example\\PyTon\\Utils")
import Utils    # noqa      # comment to ignore on top import PEP8 linting


# How to Convert Celcius to Farenheit
def changeTemp(cDegrees):
    fDegrees = float(cDegrees + 32) * 9 / 5
    print("{:0.2f} Celcius  = {:0.2f} Farenheit".format(cDegrees, fDegrees))


if __name__ == '__main__':
    cDegrees = 0
    notification = "Please input Celcius: "
    cDegrees = Utils.validateIntInput(notification, cDegrees)
    changeTemp(cDegrees)

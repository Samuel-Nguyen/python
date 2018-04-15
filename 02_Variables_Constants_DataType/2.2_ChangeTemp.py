#!python3
import imp
Utils = imp.load_source("Utils", "./Utility/Utils.py")


# How to Convert Celcius to Farenheit
def changeTemp(cDegrees):
    """
    Change degree from celcius to farenheit
    """
    fDegrees = float(cDegrees + 32) * 9 / 5
    print("{:0.2f} Celcius  = {:0.2f} Farenheit".format(cDegrees, fDegrees))


if __name__ == '__main__':
    cDegrees = 0
    notification = "Please input Celcius: "
    cDegrees = Utils.validateIntInput(notification, cDegrees)
    changeTemp(cDegrees)

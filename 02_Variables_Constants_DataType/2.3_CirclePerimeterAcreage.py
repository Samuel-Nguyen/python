#!python3
import imp
Utils = imp.load_source("Utils", "./Utility/Utils.py")
Constants = imp.load_source("Constants", "./Utility/Constants.py")


def CirclePerimeterAcreage(radius):
    """
    Calculation perimeter and acreage base on radius
    Return two item at once
    """
    perimeter = 'Perimeter p = 2 * {} * {} = {:0.2f}' \
        .format(Constants.PI, radius, radius * Constants.PI * 2)
    acreage = 'Acreage s = {:0.2f} * {} * {} = {:0.2f}' \
        .format(Constants.PI, radius, radius, Constants.PI * radius * radius)

    return perimeter, acreage


if __name__ == "__main__":
    radius = 0
    notification = "Please input radius: "
    radius = Utils.validateIntInput(notification, radius)
    p, a = CirclePerimeterAcreage(radius)
    print(p)
    print(a)

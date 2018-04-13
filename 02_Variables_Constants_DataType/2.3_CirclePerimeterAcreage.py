#!python3
import sys

sys.path.append("D:\\Samuel\\Example\\PyTon\\Utils")
import Utils    # noqa      # comment to ignore on top import PEP8 linting
PI = 3.14


def CirclePerimeterAcreage(radius):
    """
    Calculation perimeter and acreage base on radius
    Return two item at once
    """
    perimeter = 'Perimeter p = 2 * {} * {} = {:0.2f}' \
        .format(PI, radius, radius * PI * 2)
    acreage = 'Acreage s = {:0.2f} * {} * {} = {:0.2f}' \
        .format(PI, radius, radius, PI * radius * radius)

    return perimeter, acreage


if __name__ == "__main__":
    radius = 0
    notification = "Please input radius: "
    radius = Utils.validateIntInput(notification, radius)
    p, a = CirclePerimeterAcreage(radius)
    print(p)
    print(a)

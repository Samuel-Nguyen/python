#!python3
import sys

sys.path.append("D:\\Samuel\\Example\\PyTon\\Utils")
import Utils    # noqa      # comment to ignore on top import PEP8 linting


PI = 3.14


def CirclePerimeter(radius):
    return 'Perimeter p = 2 * {} * {} = {:0.2f}' \
        .format(PI, radius, radius*PI*2)


if __name__ == "__main__":
    radius = 0
    notification = "Please input radius: "
    radius = Utils.validateIntInput(notification, radius)
    print(CirclePerimeter(radius))

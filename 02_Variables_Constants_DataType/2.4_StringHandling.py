#!python3
import sys

sys.path.append("D:\\Samuel\\Example\\PyTon\\Utils")
import Utils    # noqa


def StringHandling():
    """
    Some method related with String
    """
    index = 0
    s1 = input("Please input str1: ")
    s2 = input("Please input str2: ")
    s3 = input("Please input str3: ")
    index = Utils.validateIntInput("Please input index for str1: ", index)

    print("Length of str1 = {}".format(len(s1)))
    print("Length of str2 = {}".format(len(s2)))
    print("Length of str3 = {}".format(len(s3)))
    print("str4 from index {} = {}".format(index, s1[index:]))
    print("Double s2 = {}".format(s2 * 2))


if __name__ == "__main__":
    StringHandling()

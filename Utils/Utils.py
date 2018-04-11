#!python3


def validateIntInput(notification, first):
    while True:
        try:
            first = int(input(notification))
        except ValueError:
            print("Sorry... Please input int value!")
            continue
        except NameError:
            print("Sorry... Please input int value!")
            continue
        except SyntaxError:
            print("Sorry... Please input int value!")
            continue
        else:
            break
    return first

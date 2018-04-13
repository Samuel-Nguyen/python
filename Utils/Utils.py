#!python3


def validateIntInput(notification, number):
    while True:
        try:
            number = int(input(notification))
        except ValueError:
            print("Sorry... Please input int value!")
            continue
        # except NameError:
        #     print("Sorry... Please input int value!")
        #     continue
        # except SyntaxError:
        #     print("Sorry... Please input int value!")
        #     continue
        else:
            break
    return number


def validateFloatInput(notification, number):
    while True:
        try:
            number = float(input(notification))
        except ValueError:
            print("Sorry... Please input float value!")
            continue
        # except NameError:
        #     print("Sorry... Please input float value!")
        #     continue
        # except SyntaxError:
        #     print("Sorry... Please input float value!")
        #     continue
        else:
            break
    return number


def validatePositiveFloatInput(notification, number):
    while True:
        try:
            number = float(input(notification))
            if number < 0:
                raise ValueError("Sorry... Please input positive float value!")
        except ValueError as error:
            if str(error).startswith("could not"):
                error = "Sorry... Please input float value!"
            print(error)
            continue
        # except NameError:
        #     print("Sorry... Please input float value!Name")
        #     continue
        # except SyntaxError:
        #     print("Sorry... Please input float value!Syntax")
        #     continue
        else:
            break
    return number


def validatePositiveIntInput(notification, number):
    while True:
        try:
            number = int(input(notification))
            if number < 0:
                raise ValueError("Sorry... Please input positive int value!")
        except ValueError as error:
            if str(error).startswith("could not"):
                error = "Sorry... Please input int value!"
            print(error)
            continue
        # except NameError:
        #     print("Sorry... Please input float value!Name")
        #     continue
        # except SyntaxError:
        #     print("Sorry... Please input float value!Syntax")
        #     continue
        else:
            break
    return number

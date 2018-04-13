#!python3


def calculatedMoney(quantity, price):
    """
    Calculation amount money need to pay base on quantity and price
    """
    print("Amount  = {} * {} = {}".format(quantity, price, quantity * price))


if __name__ == '__main__':
    quantity = int(input("Quantity: "))
    price = int(input("Price   : "))
    calculatedMoney(quantity, price)

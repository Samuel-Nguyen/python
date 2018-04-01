def CountDownVertical(n):
    # n = int(input("nhap vao so nguyen n: "))
    while n > 0:
        print(n)
        n -= 1
    print("Start")


def CountDownHorizontal(n):
    # n = int(input("nhap vao so nguyen n: "))
    chuoi = "n= "+str(n)+":"
    while n > 0:
        chuoi += str(n)+" "
        n -= 1
    print(chuoi)

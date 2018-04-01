import math

a, b, c = 2, 4, 5
print(input("Nhap chuoi a,b,c : ").split(" "))
# pt = a * pow(x, 2) + b * x + c
if a == 0:
    # pt=b*x+c
    if b == 0 and c != 0:
        print("phuong trinh vo nghiem")
    elif b == 0 and c == 0:
        print("phuong trinh vo so nghiem")
    else:
        x = -(c/b)
        print(x)
else:
    delta = pow(b, 2)-4*a*c
    if delta < 0:
        print("phuong trinh vo nghiem")
    elif delta == 0:
        x0 = -b/2 * a
        print("phuong trinh co nghiem kep", x0)
    else:
        x1 = (-b+math.sqrt(delta))/2*a
        x2 = (-b-math.sqrt(delta))/2*a

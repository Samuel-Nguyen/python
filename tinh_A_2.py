# A=(x**2+x+1)**n + (x**2-x+1)**n
# n=3 x=2
n = int(input("nhap n: "))
x = int(input("nhap x: "))
a = pow((pow(x, 2)+x+1), n)+pow((pow(x, 2)-x+1), n)
print("A=(x^2+x+1)^n + (x^2-x+1)^n", a)

# A=(x**2+x+1)**n + (x**2-x+1)**n
# n=3 x=2
n = int(input("nhap n: "))
x = eval(input("nhap x: "))
a1 = (x*x+x+1)
a2 = (x*x-x+1)
a = 1
for i in range(n):
    a *= a1
for o in range(n):
    a *= a2
print(a1, a2, a)

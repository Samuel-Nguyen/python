# S=(x*x+1)**n

n = int(input("n= "))
x = int(input("x= "))
s = (x*x+1)
kq = 1
for i in range(n):
    kq *= s
print(kq)

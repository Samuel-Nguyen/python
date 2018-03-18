so = int(input("nhap 1 so nguyen duong: "))
i = 1
tong = 0
while (i <= so):
    if i % 2 == 0:
        tong += i
    i += 1
print(tong)
